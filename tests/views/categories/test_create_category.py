""" Module for testing create category endpoint """

from flask import json
from tests.mocks.category import (
    VALID_CATEGORY,
    INVALID_CATEGORY_WITHOUT_NAME,
    INVALID_CATEGORY_WITH_EXISTING_NAME,
    INVALID_CATEGORY_WITH_UNEXISTING_PARENT_ID)
from tests.constants import API_BASE_URL, CONTENT_TYPE
import api.views.category


class TestCreateCategoryEndpoint:
    """ Class for testing create category endpoint """

    def test_create_category_succeeds(self, client, init_db, admin_auth_header):
        """ Testing create category """

        category_data = json.dumps(VALID_CATEGORY)
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, headers=admin_auth_header)
        message = 'Category successfully created'

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'category' in response.json['data']
        assert response.json['data']['category']['name'] == VALID_CATEGORY['name']

    def test_create_category__without_auth_token_fails(self, client, init_db):
        """ Testing create category without auth token """

        category_data = json.dumps(VALID_CATEGORY)
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, content_type=CONTENT_TYPE)
        message = 'No authorization token provided'

        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_category__with_invalid_token_fails(self, client, init_db):
        """ Testing create category with invalid token """

        category_data = json.dumps(VALID_CATEGORY)
        headers = {
            'Authorization': 'arrows',
            'Content_type': CONTENT_TYPE
        }
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, headers=headers)
        message = 'The provided authorization token is invalid'

        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_category__with_non_admin_user_fails(self, client, init_db, user_auth_header):
        """ Testing create category with a non admin user """

        category_data = json.dumps(VALID_CATEGORY)
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, headers=user_auth_header)
        message = 'Permission denied. You are not authorized to perform this action'

        assert response.status_code == 403
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_category__without_name_fails(self, client, init_db, admin_auth_header):
        """ Testing create category without category name """

        category_data = json.dumps(INVALID_CATEGORY_WITHOUT_NAME)
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, headers=admin_auth_header)
        message = 'The category name is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_category__with_existing_name_fails(self,
                                                       client,
                                                       init_db, admin_auth_header,
                                                       new_category):
        """ Testing create category with existing category name """

        new_category.save()
        category_data = json.dumps(INVALID_CATEGORY_WITH_EXISTING_NAME)
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, headers=admin_auth_header)
        message = 'The category name provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_category__with_invalid_parent_id_fails(self,
                                                           client,
                                                           init_db, admin_auth_header):
        """ Testing create category with unexisting parent ID """

        category_data = json.dumps(INVALID_CATEGORY_WITH_UNEXISTING_PARENT_ID)
        response = client.post(
            f'{API_BASE_URL}/categories', data=category_data, headers=admin_auth_header)
        message = 'The parent category provided doesn\'t exist'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
