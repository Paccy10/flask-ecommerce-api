""" Module for cart fixtures """

import pytest
from api.models.cart import Cart
from api.models.cart_item import CartItem


@pytest.fixture(scope='module')
def new_cart(init_db, new_activated_user):
    """ New cart fixture """

    new_activated_user.save()
    return Cart(
        user_id=new_activated_user.id
    )


@pytest.fixture(scope='module')
def new_cart_item(init_db, new_cart, new_product):
    """ Another brand fixture """

    new_cart.save()
    new_product.save()

    return CartItem(
        cart_id=new_cart.id,
        product_id=new_product.id,
        quantity=10
    )
