""" Module for testing get product endpoints """

import api.views.product
from tests.constants import API_BASE_URL


class TestGetProductEndpoints:
    """ Class for testing get product endpoints """

    def test_get_all_products_succeeds(self, client, init_db, new_product):
        """ Testing get all products """

        new_product.save()
        response = client.get(
            f'{API_BASE_URL}/products')
        message = 'Products successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'products' in response.json['data']
        assert 'meta' in response.json['data']
        assert len(response.json['data']['products']) == 1
        assert response.json['data']['products'][0]['name'] == new_product.name

    def test_get_all_products_with_pagination_succeeds(self,
                                                       client,
                                                       init_db,
                                                       new_product,
                                                       another_product):
        """ Testing get all products with pagination params provided """

        another_product.save()
        response = client.get(
            f'{API_BASE_URL}/products?page=1&limit=1')
        message = 'Products successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'products' in response.json['data']
        assert 'meta' in response.json['data']
        assert len(response.json['data']['products']) == 1
        assert response.json['data']['meta']['previous_page'] is None

    def test_get_all_products_with_prev_page_succeeds(self,
                                                      client,
                                                      init_db,
                                                      new_product,
                                                      another_product):
        """ Testing get all products with previous page """

        another_product.save()
        response = client.get(
            f'{API_BASE_URL}/products?page=2&limit=1')
        message = 'Products successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'products' in response.json['data']
        assert 'meta' in response.json['data']
        assert len(response.json['data']['products']) == 1
        assert response.json['data']['meta']['next_page'] is None

    def test_get_all_products_with_string_page_nbr_fails(self,
                                                         client,
                                                         init_db,
                                                         new_product,
                                                         another_product):
        """ Testing get all products with a string page number """

        another_product.save()
        response = client.get(
            f'{API_BASE_URL}/products?page=ab&limit=1')
        message = 'The page must be a positive integer greater than 0'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_get_all_products_with_negative_page_nbr_fails(self,
                                                           client,
                                                           init_db,
                                                           new_product,
                                                           another_product):
        """ Testing get all products with a negative page number """

        another_product.save()
        response = client.get(
            f'{API_BASE_URL}/products?page=-1&limit=1')
        message = 'The page must be a positive integer greater than 0'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_get_single_product_succeeds(self, client, init_db, new_product):
        """ Testing get a single product by ID """

        new_product.save()
        response = client.get(
            f'{API_BASE_URL}/products/{new_product.id}')
        message = 'Product successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'product' in response.json['data']
        assert response.json['data']['product']['name'] == new_product.name

    def test_get_single_product_with_unexisting_product_id_fails(self,
                                                                 client,
                                                                 init_db):
        """ Testing get a single product by ID with an unexisting product ID """

        response = client.get(
            f'{API_BASE_URL}/products/10')
        message = 'Product not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
