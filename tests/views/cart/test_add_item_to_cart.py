""" Module for testing add item to the cart endpoint """

from flask import json
from tests.mocks.cart import (VALID_CART_ITEM,
                              INVALID_CART_ITEM_WITHOUT_PRODUCT_ID,
                              INVALID_CART_ITEM_WITH_STRING_PRODUCT_ID,
                              INVALID_CART_ITEM_WITH_UNEXISTED_PRODUCT_ID,
                              INVALID_CART_ITEM_WITHOUT_QUANTITY,
                              INVALID_CART_ITEM_WITH_STRING_QUANTITY,
                              INVALID_CART_ITEM_WITH_UNVAILABLE_QUANTITY)
from tests.constants import API_BASE_URL, CONTENT_TYPE
import api.views.cart


class TestAddCartItemEndpoint:
    """ Class for testing add ietm to the cart endpoint """

    def test_add_item_to_cart_succeeds(self,
                                       client,
                                       init_db,
                                       user_auth_header,
                                       new_cart,
                                       new_product):
        """ Testing add item to the cart """

        new_cart.save()
        new_product.save()
        cart_item_data = json.dumps(VALID_CART_ITEM)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'Item successfully added to the cart'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'items' in response.json['data']['cart']
        assert len(response.json['data']['cart']['items']) == 1
        assert response.json['data']['cart']['items'][0]['quantity'] == VALID_CART_ITEM['quantity']

    def test_update_cart_item_succeeds(self,
                                       client,
                                       init_db,
                                       user_auth_header,
                                       new_cart,
                                       new_product):
        """ Testing add item to the cart """

        cart_item_data = json.dumps(VALID_CART_ITEM)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'Item successfully added to the cart'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'items' in response.json['data']['cart']
        assert len(response.json['data']['cart']['items']) == 1
        assert response.json['data']['cart']['items'][0]['quantity'] == \
            VALID_CART_ITEM['quantity'] + 1

    def test_add_item_to_cart_without_product_id_fails(self,
                                                       client,
                                                       init_db,
                                                       user_auth_header,
                                                       new_cart,
                                                       new_product):
        """ Testing add item to the cart without product ID """

        new_cart.save()
        new_product.save()
        cart_item_data = json.dumps(INVALID_CART_ITEM_WITHOUT_PRODUCT_ID)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'The product ID is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_item_to_cart_with_string_product_id_fails(self,
                                                           client,
                                                           init_db,
                                                           user_auth_header,
                                                           new_cart,
                                                           new_product):
        """ Testing add item to the cart with string product ID """

        new_cart.save()
        new_product.save()
        cart_item_data = json.dumps(INVALID_CART_ITEM_WITH_STRING_PRODUCT_ID)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'The product ID should be a positive integer'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_item_to_cart_with_unexisted_product_id_fails(self,
                                                              client,
                                                              init_db,
                                                              user_auth_header,
                                                              new_cart):
        """ Testing add item to the cart with unexisted product ID """

        new_cart.save()
        cart_item_data = json.dumps(
            INVALID_CART_ITEM_WITH_UNEXISTED_PRODUCT_ID)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'The product ID provided doesn\'t exist'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_item_to_cart_without_quantity_fails(self,
                                                     client,
                                                     init_db,
                                                     user_auth_header,
                                                     new_cart,
                                                     new_product):
        """ Testing add item to the cart without quantity """

        new_cart.save()
        new_product.save()
        cart_item_data = json.dumps(INVALID_CART_ITEM_WITHOUT_QUANTITY)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'The product quantity is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_item_to_cart_with_string_quantity_fails(self,
                                                         client,
                                                         init_db,
                                                         user_auth_header,
                                                         new_cart,
                                                         new_product):
        """ Testing add item to the cart with string quantity """

        new_cart.save()
        new_product.save()
        cart_item_data = json.dumps(INVALID_CART_ITEM_WITH_STRING_QUANTITY)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'The product quantity should be a positive integer'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_item_to_cart_with_unvailable_quantity_fails(self,
                                                             client,
                                                             init_db,
                                                             user_auth_header,
                                                             new_cart,
                                                             new_product):
        """ Testing add item to the cart with unvailable quantity """

        new_cart.save()
        new_product.save()
        cart_item_data = json.dumps(INVALID_CART_ITEM_WITH_UNVAILABLE_QUANTITY)
        response = client.post(
            f'{API_BASE_URL}/auth/cart', data=cart_item_data, headers=user_auth_header)
        message = 'The product is not available'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
