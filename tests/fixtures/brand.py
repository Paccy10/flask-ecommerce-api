""" Module for brand fixtures """

import pytest
from api.models.brand import Brand


@pytest.fixture(scope='module')
def new_brand(init_db):
    """ New brand fixture """

    return Brand(
        name='nike',
        description='American company'
    )


@pytest.fixture(scope='module')
def another_brand(init_db):
    """ Another brand fixture """

    return Brand(
        name='puma',
        description=''
    )
