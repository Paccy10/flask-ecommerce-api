""" Module for testing update and delete brand endpoints """

from flask import json
import api.views.brand
from tests.mocks.brand import (
    UPDATED_VALID_BRAND, UPDATED_BRAND_WITH_EXISTING_NAME)
from tests.constants import API_BASE_URL


class TestUpdateAndDeleteBrandEndpoints:
    """ Class for testing update and delete brand endpoints """

    def test_update_brand_succeeds(self, client, init_db, admin_auth_header, new_brand):
        """ Testing update brand """

        new_brand.save()

        brand_data = json.dumps(UPDATED_VALID_BRAND)
        response = client.put(
            f'{API_BASE_URL}/brands/{new_brand.id}',
            data=brand_data, headers=admin_auth_header)
        message = 'Brand successfully updated'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'brand' in response.json['data']
        assert response.json['data']['brand']['name'] == UPDATED_VALID_BRAND['name']

    def test_update_brand_with_unexisting_id_fails(self, client, init_db, admin_auth_header):
        """ Testing update brand with an unexisting brand ID """

        brand_data = json.dumps(UPDATED_VALID_BRAND)
        response = client.put(
            f'{API_BASE_URL}/brands/2',
            data=brand_data, headers=admin_auth_header)
        message = 'Brand not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_update_brand_with_existing_name_fails(self,
                                                   client,
                                                   init_db,
                                                   admin_auth_header,
                                                   new_brand,
                                                   another_brand):
        """ Testing update brand with an existing brand name """

        new_brand.save()
        another_brand.save()

        brand_data = json.dumps(UPDATED_BRAND_WITH_EXISTING_NAME)
        response = client.put(
            f'{API_BASE_URL}/brands/{new_brand.id}',
            data=brand_data, headers=admin_auth_header)
        message = 'The brand name provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_delete_brand_succeeds(self, client, init_db, admin_auth_header):
        """ Testing delete brand """

        response = client.delete(
            f'{API_BASE_URL}/brands/2', headers=admin_auth_header)
        message = 'Brand successfully deleted'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message

    def test_delete_brand_with_unexisting_id_fails(self, client, init_db, admin_auth_header):
        """ Testing delete brand with an unexisting brand ID """

        response = client.delete(
            f'{API_BASE_URL}/brands/3', headers=admin_auth_header)
        message = 'Brand not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
