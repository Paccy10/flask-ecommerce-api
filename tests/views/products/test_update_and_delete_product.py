""" Module for testing update and delete product endpoints """

from flask import json
import api.views.product
from tests.mocks.product import (
    UPDATED_VALID_PRODUCT, UPDATED_INVALID_PRODUCT_WITH_EXISTED_NAME)
from tests.constants import API_BASE_URL


class TestUpdateAndDeleteProductEndpoints:
    """ Class for testing update and delete product endpoints """

    def test_update_product_succeeds(self, client, init_db, admin_auth_header, new_product):
        """ Testing update product """

        new_product.save()

        product_data = json.dumps(UPDATED_VALID_PRODUCT)
        response = client.put(
            f'{API_BASE_URL}/products/{new_product.id}',
            data=product_data, headers=admin_auth_header)
        message = 'Product successfully updated'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'product' in response.json['data']
        assert response.json['data']['product']['name'] == UPDATED_VALID_PRODUCT['name']

    def test_update_product_with_unexisting_id_fails(self, client, init_db, admin_auth_header):
        """ Testing update product with an unexisting product ID """

        product_data = json.dumps(UPDATED_VALID_PRODUCT)
        response = client.put(
            f'{API_BASE_URL}/products/2',
            data=product_data, headers=admin_auth_header)
        message = 'Product not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_update_product_with_existed_name_fails(self,
                                                    client,
                                                    init_db,
                                                    admin_auth_header,
                                                    new_product,
                                                    another_product):
        """ Testing update product with an existed product name """

        new_product.save()
        another_product.save()

        product_data = json.dumps(UPDATED_INVALID_PRODUCT_WITH_EXISTED_NAME)
        response = client.put(
            f'{API_BASE_URL}/products/{another_product.id}',
            data=product_data, headers=admin_auth_header)
        message = 'The product name provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_delete_product_succeeds(self, client, init_db, admin_auth_header):
        """ Testing delete product """

        response = client.delete(
            f'{API_BASE_URL}/products/2', headers=admin_auth_header)
        message = 'Product successfully deleted'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message

    def test_delete_product_with_unexisted_id_fails(self, client, init_db, admin_auth_header):
        """ Testing delete product with an unexisting product ID """

        response = client.delete(
            f'{API_BASE_URL}/products/3', headers=admin_auth_header)
        message = 'Product not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
