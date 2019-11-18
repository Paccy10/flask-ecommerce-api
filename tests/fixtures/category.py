""" Module for category fixtures """

import pytest
from api.models.category import Category


@pytest.fixture(scope='module')
def new_category(init_db):
    """ New category fixture """

    return Category(
        name='laptops',
        description='Personal portable computers'
    )
