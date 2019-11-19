""" Module for testing create category endpoint """

from flask import json
from tests.mocks.brand import (
    VALID_BRAND, INVALID_BRAND_WITHOUT_NAME, INVALID_BRAND_WITH_EXISTING_NAME)
from tests.constants import API_BASE_URL, CONTENT_TYPE
import api.views.brand


class TestCreateBrandEndpoint:
    """ Class for testing create brand endpoint """

    def test_create_brand_succeeds(self, client, init_db, admin_auth_header):
        """ Testing create brand """

        brand_data = json.dumps(VALID_BRAND)
        response = client.post(
            f'{API_BASE_URL}/brands', data=brand_data, headers=admin_auth_header)
        message = 'Brand successfully created'

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'brand' in response.json['data']
        assert response.json['data']['brand']['name'] == VALID_BRAND['name']

    def test_create_brand_without_name_fails(self, client, init_db, admin_auth_header):
        """ Testing create brand without category name """

        brand_data = json.dumps(INVALID_BRAND_WITHOUT_NAME)
        response = client.post(
            f'{API_BASE_URL}/brands', data=brand_data, headers=admin_auth_header)
        message = 'The brand name is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_brand_with_existing_name_fails(self,
                                                   client,
                                                   init_db, admin_auth_header,
                                                   new_brand):
        """ Testing create brand with existing category name """

        new_brand.save()
        brand_data = json.dumps(INVALID_BRAND_WITH_EXISTING_NAME)
        response = client.post(
            f'{API_BASE_URL}/brands', data=brand_data, headers=admin_auth_header)
        message = 'The brand name provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
