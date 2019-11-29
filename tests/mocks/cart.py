""" Module for cart item mocking data """

VALID_CART_ITEM = {
    'product_id': 1,
    'quantity': 1
}

INVALID_CART_ITEM_WITHOUT_PRODUCT_ID = {
    'quantity': 1
}

INVALID_CART_ITEM_WITH_STRING_PRODUCT_ID = {
    'product_id': '',
    'quantity': 1
}

INVALID_CART_ITEM_WITH_UNEXISTED_PRODUCT_ID = {
    'product_id': 2,
    'quantity': 1
}

INVALID_CART_ITEM_WITHOUT_QUANTITY = {
    'product_id': 1
}

INVALID_CART_ITEM_WITH_STRING_QUANTITY = {
    'product_id': 1,
    'quantity': ''
}

INVALID_CART_ITEM_WITH_UNVAILABLE_QUANTITY = {
    'product_id': 1,
    'quantity': 60
}
