""" Module for authorization fixture """

import pytest
from api.schemas.user import UserSchema
from api.utilities.generate_token import generate_auth_token


@pytest.fixture(scope='module')
def admin_auth_header(init_db, new_admin):
    """ Admin auth header fixture """

    new_admin.save()

    user_schema = UserSchema()
    user_data = user_schema.dump(new_admin)
    token = generate_auth_token(user_data)
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }


@pytest.fixture(scope='module')
def user_auth_header(init_db, new_activated_user):
    """ Admin auth header fixture """

    new_activated_user.save()

    user_schema = UserSchema()
    user_data = user_schema.dump(new_activated_user)
    token = generate_auth_token(user_data)
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
