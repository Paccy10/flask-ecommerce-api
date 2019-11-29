""" Module for cart validators """

from flask import request
from api.models.product import Product
from . import raise_validation_error, is_positive_integer


class CartValidators:
    """ Cart validators class """

    @classmethod
    def validate_product_id(cls, product_id):
        """ Validates the product ID """

        if product_id is None:
            raise_validation_error('The product ID is required')

        if not is_positive_integer(product_id):
            raise_validation_error(
                'The product ID should be a positive integer')

        product = Product.find_by_id(product_id)

        if not product:
            raise_validation_error('The product ID provided doesn\'t exist')

    @classmethod
    def validate_quantity(cls, quantity):
        """ Validates the product ID """

        if quantity is None:
            raise_validation_error('The product quantity is required')

        if not is_positive_integer(quantity):
            raise_validation_error(
                'The product quantity should be a positive integer')

    @classmethod
    def validate_item(cls, data: dict):
        """ Validates the cart item """

        product_id = data.get('product_id')
        quantity = data.get('quantity')

        cls.validate_product_id(product_id)
        cls.validate_quantity(quantity)

        product = Product.find_by_id(product_id)
        product_quantity = product.quantity
        user_needed_quantity = quantity

        if product_quantity - user_needed_quantity < 0:
            raise_validation_error('The product is not available')
