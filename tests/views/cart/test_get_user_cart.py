""" Module for testing get cart endpoints """

import api.views.cart
from tests.constants import API_BASE_URL


class TestGetCartEndpoints:
    """ Class for testing get user cart endpoints """

    def test_get_all_cart_succeeds(self, client, init_db, new_cart, user_auth_header):
        """ Testing get user cart categories """

        new_cart.save()
        response = client.get(
            f'{API_BASE_URL}/auth/cart', headers=user_auth_header)
        message = 'Cart successfully fetched'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'cart' in response.json['data']
        assert len(response.json['data']['cart']) == 3
