""" Module for testing create user endpoint """

import time
from flask import json
from tests.mocks.user import (
    VALID_USER,
    INVALID_USER_WTHOUT_FIRSTNAME,
    INVALID_USER_WTHOUT_LASTNAME,
    INVALID_USER_WTHOUT_EMAIL,
    INVALID_USER_WTHOUT_PASSWORD,
    INVALID_USER_WTH_INVALID_EMAIL,
    INVALID_USER_WTH_INVALID_PASSWORD_LENGTH,
    INVALID_USER_WTH_PASSWORD_WITHOUT_CAPITAL_LETTER,
    INVALID_USER_WTH_PASSWORD_WITHOUT_SMALL_LETTER,
    INVALID_USER_WTH_PASSWORD_WITHOUT_DIGIT,
    INVALID_USER_ALREADY_EXISTS)
from tests.constants import API_BASE_URL, CONTENT_TYPE
import api.views.user
from api.utilities.generate_token import generate_user_token


class TestUserSignupEndpoint:
    """ Class for testing user signup resource """

    def test_user_signup_succeeds(self, client, init_db):
        """ Testing user signup """

        user_data = json.dumps(VALID_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'User successfully created. Please check your email to continue.'

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == message

    def test_user_signup_without_firstname_fails(self, client, init_db):
        """ Testing user signup without firstname """

        user_data = json.dumps(INVALID_USER_WTHOUT_FIRSTNAME)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The firstname is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_without_lastname_fails(self, client, init_db):
        """ Testing user signup without lastname """

        user_data = json.dumps(INVALID_USER_WTHOUT_LASTNAME)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The lastname is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_without_email_fails(self, client, init_db):
        """ Testing user signup without email """

        user_data = json.dumps(INVALID_USER_WTHOUT_EMAIL)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The email is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_without_password_fails(self, client, init_db):
        """ Testing user signup without password """

        user_data = json.dumps(INVALID_USER_WTHOUT_PASSWORD)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The password is required'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_with_invalid_email_fails(self, client, init_db):
        """ Testing user signup with invalid email """

        user_data = json.dumps(INVALID_USER_WTH_INVALID_EMAIL)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The email provided is not valid'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_with_existing_email_fails(self, client, init_db, new_user):
        """ Testing user signup with existing email """

        new_user.save()
        user_data = json.dumps(INVALID_USER_ALREADY_EXISTS)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The email provided already exists'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_with_invalid_password_length_fails(self, client, init_db):
        """ Testing user signup with invalid password length """

        user_data = json.dumps(INVALID_USER_WTH_INVALID_PASSWORD_LENGTH)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The password must be at least 8 characters'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_with_password_without_capital_letter_fails(self, client, init_db):
        """ Testing user signup with password without a capital letter """

        user_data = json.dumps(
            INVALID_USER_WTH_PASSWORD_WITHOUT_CAPITAL_LETTER)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The password must have at least one uppercase letter'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_with_password_without_small_letter_fails(self, client, init_db):
        """ Testing user signup with password without a capital letter """

        user_data = json.dumps(
            INVALID_USER_WTH_PASSWORD_WITHOUT_SMALL_LETTER)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The password must have at least one lowercase letter'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_signup_with_password_without_digit_fails(self, client, init_db):
        """ Testing user signup with password without a digit """

        user_data = json.dumps(
            INVALID_USER_WTH_PASSWORD_WITHOUT_DIGIT)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)
        message = 'The password must have at least one digit'

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_user_activation_succeeds(self, client, new_user):
        """ Testing User activation """

        new_user.save()
        token = generate_user_token(new_user.id)
        response = client.get(
            f'{API_BASE_URL}/auth/activate/{token}')

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'User successfully activated'
        assert 'token' in response.json['data']
        assert 'user' in response.json['data']
        assert response.json['data']['user']['email'] == new_user.email

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
