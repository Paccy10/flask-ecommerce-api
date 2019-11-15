""" Module for user fixtures """

import pytest
from api.models.user import User


@pytest.fixture(scope='module')
def new_user(init_db):
    """ New user fixture """
    return User(
        firstname='Pacifique',
        lastname='Ndayisenga',
        email='pacifiqueclement@gmail.com',
        password='Password1234',
    )


@pytest.fixture(scope='module')
def new_activated_user(init_db):
    """ New user fixture """
    return User(
        firstname='Pacifique',
        lastname='Ndayisenga',
        email='pacifiqueclement10@gmail.com',
        password='Password1234',
        is_activated=True
    )
