""" Module for testing activate user endpoint """

import time
from flask import json
from tests.constants import API_BASE_URL
import api.views.user
from api.utilities.generate_token import generate_user_token


class TestUserActivationEndpoint:
    """ Class for testing user activation resource """

    def test_user_activation_succeeds(self, client, new_user):
        """ Testing User activation """

        new_user.save()
        token = generate_user_token(new_user.id)
        response = client.get(
            f'{API_BASE_URL}/auth/activate/{token}')

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'User successfully activated'

    def test_user_activation_with_invalid_token_fails(self, client):
        """ Testing User activation with invalid token """

        token = generate_user_token(5)
        response = client.get(
            f'{API_BASE_URL}/auth/activate/{token}')

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Account activation token is invalid'

    def test_user_activation_with_expired_token_fails(self, client, new_user):
        """ Testing User activation with expired token """

        new_user.save()
        token = generate_user_token(new_user.id, expires_sec=0)
        time.sleep(1)
        response = client.get(
            f'{API_BASE_URL}/auth/activate/{token}')

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Account activation token is invalid'

    def test_user_activation_already_activated_fails(self, client, new_user):
        """ Testing User activation already activated """

        new_user.save()
        token = generate_user_token(new_user.id)
        response = client.get(
            f'{API_BASE_URL}/auth/activate/{token}')

        response2 = client.get(
            f'{API_BASE_URL}/auth/activate/{token}')

        assert response2.status_code == 400
        assert response2.json['status'] == 'error'
        assert response2.json['message'] == 'User account already activated'
