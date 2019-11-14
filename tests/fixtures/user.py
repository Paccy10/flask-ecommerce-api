""" Module for user fixtures """

import pytest
from api.models.user import User


@pytest.fixture(scope='module')
def new_user(init_db):
    """ New user fixture """
    return User(
        firstname='Pacifique',
        lastname='Ndayisenga',
        email='pacifique.ndayisenga@andela.com',
        password='Password1234',
    )
