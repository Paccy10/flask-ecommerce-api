""" Module for tests configuration """

import pytest
from config.server import application
from api.models.database import db

pytest_plugins = ['tests.fixtures.user']


@pytest.fixture(scope='module')
def app():
    """ Setup flask test application """

    return application


@pytest.fixture(scope='module')
def init_db():
    """ Initialize the test database """

    db.drop_all()
    db.create_all()
    yield db
    db.session.close()
