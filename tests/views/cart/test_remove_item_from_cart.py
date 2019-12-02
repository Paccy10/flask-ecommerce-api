""" Module for testing get cart endpoints """

import api.views.cart
from tests.constants import API_BASE_URL


class TestDeleteCartItemEndpoints:
    """ Class for testing remove item from cart endpoint """

    def test_delete_cart_item_succeeds(self, client, init_db, new_cart_item, user_auth_header):
        """ Testing get user cart categories """

        new_cart_item.save()
        response = client.delete(
            f'{API_BASE_URL}/auth/cart/items/{new_cart_item.id}', headers=user_auth_header)
        message = 'Item successfully removed from the cart'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
        assert 'cart' in response.json['data']
        assert len(response.json['data']['cart']['items']) == 0

    def test_delete_cart_item_with_unexisted_id_fails(self, client, init_db, user_auth_header):
        """ Testing get user cart categories """

        response = client.delete(
            f'{API_BASE_URL}/auth/cart/items/2', headers=user_auth_header)
        message = 'Cart Item not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
