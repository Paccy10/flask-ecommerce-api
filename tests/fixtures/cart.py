""" Module for cart fixtures """

import pytest
from api.models.cart import Cart


@pytest.fixture(scope='module')
def new_cart(init_db, new_activated_user):
    """ New cart fixture """

    new_activated_user.save()
    return Cart(
        user_id=new_activated_user.id
    )


# @pytest.fixture(scope='module')
# def another_brand(init_db):
#     """ Another brand fixture """

#     return Brand(
#         name='puma',
#         description=''
#     )
