""" Module for testing update and delete category endpoints """

from flask import json
import api.views.category
from tests.mocks.category import (
    UPDATED_VALID_CATEGORY, UPDATED_CATEGORY_WITH_EXISTING_NAME)
from tests.constants import API_BASE_URL


class TestUpdateAndDeleteCategoryEndpoints:
    """ Class for testing update and delete category endpoints """

    def test_update_category_succeeds(self, client, init_db, admin_auth_header, new_category):
        """ Testing update category """

        new_category.save()

        category_data = json.dumps(UPDATED_VALID_CATEGORY)
        response = client.put(
            f'{API_BASE_URL}/categories/{new_category.id}',
            data=category_data, headers=admin_auth_header)
        message = 'Category successfully updated'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'category' in response.json['data']
        assert response.json['data']['category']['name'] == UPDATED_VALID_CATEGORY['name']

    def test_update_category_with_unexisting_id_fails(self, client, init_db, admin_auth_header):
        """ Testing update category with an unexisting category ID """

        category_data = json.dumps(UPDATED_VALID_CATEGORY)
        response = client.put(
            f'{API_BASE_URL}/categories/2',
            data=category_data, headers=admin_auth_header)
        message = 'Category not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_update_category_with_existing_name_fails(self,
                                                      client,
                                                      init_db,
                                                      admin_auth_header,
                                                      new_category,
                                                      another_category):
        """ Testing update category with an existing category name """

        new_category.save()
        another_category.save()

        category_data = json.dumps(UPDATED_CATEGORY_WITH_EXISTING_NAME)
        response = client.put(
            f'{API_BASE_URL}/categories/{new_category.id}',
            data=category_data, headers=admin_auth_header)
        message = 'The category name provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_delete_category_succeeds(self, client, init_db, admin_auth_header):
        """ Testing delete category """

        response = client.delete(
            f'{API_BASE_URL}/categories/2', headers=admin_auth_header)
        message = 'Category successfully deleted'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message

    def test_delete_category_with_unexisting_id_fails(self, client, init_db, admin_auth_header):
        """ Testing delete category with an unexisting category ID """

        response = client.delete(
            f'{API_BASE_URL}/categories/3', headers=admin_auth_header)
        message = 'Category not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
