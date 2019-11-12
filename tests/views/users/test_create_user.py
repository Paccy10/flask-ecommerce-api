""" Module for testing create user endpoint """

from flask import json
from tests.mocks.user import (VALID_USER)
from tests.constants import API_BASE_URL, CONTENT_TYPE
import api.views.user


class TestUserSignupEndpoint:
    """ Class for testing user signup resource """

    def test_user_signup_succeeds(self, client, init_db):
        """ Testing user signup succeeds """

        user_data = json.dumps(VALID_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'User successfully created. Please check your email to continue.'

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == message
