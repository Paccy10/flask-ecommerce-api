""" Module for testing get category endpoints """

import api.views.category
from tests.constants import API_BASE_URL


class TestGetCategoryEndpoints:
    """ Class for testing get category endpoints """

    def test_get_all_categories_succeeds(self, client, init_db, new_category):
        """ Testing get all categories """

        new_category.save()
        response = client.get(
            f'{API_BASE_URL}/categories')
        message = 'Categories successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'categories' in response.json['data']
        assert len(response.json['data']['categories']) == 1
        assert response.json['data']['categories'][0]['name'] == new_category.name

    def test_get_single_category_succeeds(self, client, init_db, new_category):
        """ Testing get a single category by ID """

        new_category.save()
        response = client.get(
            f'{API_BASE_URL}/categories/{new_category.id}')
        message = 'Category successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'category' in response.json['data']
        assert response.json['data']['category']['name'] == new_category.name

    def test_get_single_category_with_unexisting_category_id_fails(self,
                                                                   client,
                                                                   init_db):
        """ Testing get a single category by ID with an unexisting category ID """

        response = client.get(
            f'{API_BASE_URL}/categories/2')
        message = 'Category not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
