""" Module for testing get brand endpoints """

import api.views.brand
from tests.constants import API_BASE_URL


class TestGetBrandEndpoints:
    """ Class for testing get brand endpoints """

    def test_get_all_brands_succeeds(self, client, init_db, new_brand):
        """ Testing get all brands """

        new_brand.save()
        response = client.get(
            f'{API_BASE_URL}/brands')
        message = 'Brands successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'brands' in response.json['data']
        assert len(response.json['data']['brands']) == 1
        assert response.json['data']['brands'][0]['name'] == new_brand.name

    def test_get_single_brand_succeeds(self, client, init_db, new_brand):
        """ Testing get a single brand by ID """

        new_brand.save()
        response = client.get(
            f'{API_BASE_URL}/brands/{new_brand.id}')
        message = 'Brand successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'brand' in response.json['data']
        assert response.json['data']['brand']['name'] == new_brand.name

    def test_get_single_brand_with_unexisting_brand_id_fails(self,
                                                             client,
                                                             init_db):
        """ Testing get a single brand by ID with an unexisting brand ID """

        response = client.get(
            f'{API_BASE_URL}/brands/2')
        message = 'Brand not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
