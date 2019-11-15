""" Module for testing reset user password endpoints """

import time
from flask import json
from tests.constants import API_BASE_URL, CONTENT_TYPE
from tests.mocks.user import (
    RESET_REQUEST_USER, UNEXISTED_RESET_REQUEST_USER, RESET_PASSWORD_NEW_PASSWORD)
import api.views.user
from api.utilities.generate_token import generate_user_token


class TestPasswordResetEndpoints:
    """ Class for testing user password reset resources """

    def test_reset_request_succeeds(self, client, init_db, new_activated_user):
        """ Testing reset request """

        new_activated_user.save()
        user_data = json.dumps(RESET_REQUEST_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/reset-password', data=user_data, content_type=CONTENT_TYPE)
        message = 'Request successfully submitted. Please check your email to continue.'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message

    def test_reset_request_with_unexisted_user_fails(self, client, init_db):
        """ Testing reset request with unexisted user """

        user_data = json.dumps(UNEXISTED_RESET_REQUEST_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/reset-password', data=user_data, content_type=CONTENT_TYPE)
        message = 'User not found'

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_reset_password_succeeds(self, client, init_db, new_activated_user):
        """ Testing reset password """

        new_activated_user.save()
        user_data = json.dumps(RESET_PASSWORD_NEW_PASSWORD)
        token = generate_user_token(new_activated_user.id)

        response = client.patch(
            f'{API_BASE_URL}/auth/reset-password/{token}',
            data=user_data, content_type=CONTENT_TYPE)
        message = 'User password successfully changed'

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == message

    def test_reset_password_with_invalid_token_fails(self, client, init_db, new_activated_user):
        """ Testing reset password with invalid token """

        new_activated_user.save()
        user_data = json.dumps(RESET_PASSWORD_NEW_PASSWORD)
        token = generate_user_token(new_activated_user.id, expires_sec=0)
        time.sleep(1)

        response = client.patch(
            f'{API_BASE_URL}/auth/reset-password/{token}',
            data=user_data, content_type=CONTENT_TYPE)
        message = 'Password reset token is invalid'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message
