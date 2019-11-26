""" Module for testing create product endpoint """

from flask import json
from tests.mocks.product import (VALID_PRODUCT,
                                 INVALID_PRODUCT_WITHOUT_NAME,
                                 INVALID_PRODUCT_WITH_EXISTING_NAME,
                                 INVALID_PRODUCT_WITH_STRING_IMAGE,
                                 INVALID_PRODUCT_WITH_INVALID_IMAGE,
                                 INVALID_PRODUCT_WITHOUT_IMAGE,
                                 INVALID_PRODUCT_WITH_INVALID_OTHER_IMAGES,
                                 INVALID_PRODUCT_WITHOUT_CATEGORY_ID,
                                 INVALID_PRODUCT_WITH_INVALID_CATEGORY_ID,
                                 INVALID_PRODUCT_WITH_UNEXISTED_CATEGORY_ID,
                                 INVALID_PRODUCT_WITH_INVALID_BRAND_ID,
                                 INVALID_PRODUCT_WITH_UNEXISTED_BRAND_ID,
                                 INVALID_PRODUCT_WITHOUT_PRICE,
                                 INVALID_PRODUCT_WITH_INVALID_PRICE,
                                 INVALID_PRODUCT_WITHOUT_QUANTITY,
                                 INVALID_PRODUCT_WITH_INVALID_QUANTITY)
from tests.constants import API_BASE_URL, CONTENT_TYPE
import api.views.product


class TestCreateProductEndpoint:
    """ Class for testing create product endpoint """

    def test_create_product_succeeds(self,
                                     client,
                                     init_db,
                                     admin_auth_header,
                                     new_category,
                                     new_brand):
        """ Testing create product """

        new_category.save()
        new_brand.save()
        product_data = json.dumps(VALID_PRODUCT)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'Product successfully created'

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'product' in response.json['data']
        assert response.json['data']['product']['name'] == VALID_PRODUCT['name']

    def test_create_product_without_name_fails(self, client, init_db, admin_auth_header):
        """ Testing create product without name """

        product_data = json.dumps(INVALID_PRODUCT_WITHOUT_NAME)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The product name is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_existing_name_fails(self,
                                                     client,
                                                     init_db,
                                                     admin_auth_header,
                                                     new_product):
        """ Testing create product with existing name """

        new_product.save()
        product_data = json.dumps(INVALID_PRODUCT_WITH_EXISTING_NAME)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The product name provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_without_image_fails(self, client, init_db, admin_auth_header):
        """ Testing create product without image """

        product_data = json.dumps(INVALID_PRODUCT_WITHOUT_IMAGE)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The product main image is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_string_image_fails(self,
                                                    client,
                                                    init_db,
                                                    admin_auth_header):
        """ Testing create product with string image """

        product_data = json.dumps(INVALID_PRODUCT_WITH_STRING_IMAGE)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The image must be an object which has a url and a public_id'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_invalid_image_fails(self,
                                                     client,
                                                     init_db,
                                                     admin_auth_header):
        """ Testing create product with invalid image """

        product_data = json.dumps(INVALID_PRODUCT_WITH_INVALID_IMAGE)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The image should have a url and a public_id'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_invalid_other_images_fails(self,
                                                            client,
                                                            init_db,
                                                            admin_auth_header):
        """ Testing create product with invalid other images """

        product_data = json.dumps(INVALID_PRODUCT_WITH_INVALID_OTHER_IMAGES)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The image must be an object which has a url and a public_id'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_without_category_ID_fails(self,
                                                      client,
                                                      init_db,
                                                      admin_auth_header):
        """ Testing create product without category ID """

        product_data = json.dumps(INVALID_PRODUCT_WITHOUT_CATEGORY_ID)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The category ID is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_invalid_category_ID_fails(self,
                                                           client,
                                                           init_db,
                                                           admin_auth_header):
        """ Testing create product with invalid category ID """

        product_data = json.dumps(INVALID_PRODUCT_WITH_INVALID_CATEGORY_ID)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The category ID should be a positive integer'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_unexisted_category_ID_fails(self,
                                                             client,
                                                             init_db,
                                                             admin_auth_header):
        """ Testing create product with unexisted category ID """

        product_data = json.dumps(INVALID_PRODUCT_WITH_UNEXISTED_CATEGORY_ID)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The category ID provided doesn\'t exist'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_invalid_brand_ID_fails(self,
                                                        client,
                                                        init_db,
                                                        admin_auth_header):
        """ Testing create product with invalid brand ID """

        product_data = json.dumps(INVALID_PRODUCT_WITH_INVALID_BRAND_ID)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The brand ID should be a positive integer'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_unexisted_brand_ID_fails(self,
                                                          client,
                                                          init_db,
                                                          admin_auth_header):
        """ Testing create product with unexisted brand ID """

        product_data = json.dumps(INVALID_PRODUCT_WITH_UNEXISTED_BRAND_ID)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The brand ID provided doesn\'t exist'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_without_price_fails(self, client, init_db, admin_auth_header):
        """ Testing create product without price """

        product_data = json.dumps(INVALID_PRODUCT_WITHOUT_PRICE)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The price is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_invalid_price_fails(self,
                                                     client,
                                                     init_db,
                                                     admin_auth_header):
        """ Testing create product with invalid price """

        product_data = json.dumps(INVALID_PRODUCT_WITH_INVALID_PRICE)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The price must be a positive number'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_without_quantity_fails(self, client, init_db, admin_auth_header):
        """ Testing create product without quantity """

        product_data = json.dumps(INVALID_PRODUCT_WITHOUT_QUANTITY)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The quantity is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_product_with_invalid_quantity_fails(self,
                                                        client,
                                                        init_db,
                                                        admin_auth_header):
        """ Testing create product with invalid quantity """

        product_data = json.dumps(INVALID_PRODUCT_WITH_INVALID_QUANTITY)
        response = client.post(
            f'{API_BASE_URL}/products', data=product_data, headers=admin_auth_header)
        message = 'The quantity must be a positive integer'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
