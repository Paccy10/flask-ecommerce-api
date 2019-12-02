""" Module for the Cart Item Schema """

from marshmallow import fields
from api.utilities.helpers.constants import EXCLUDED_FIELDS
from .base import BaseSchema
from .product import ProductSchema


class CartItemSchema(BaseSchema):
    """ CartItem Schema Class """

    excluded_fields = EXCLUDED_FIELDS.copy()
    excluded_fields.extend(
        ['quantity', 'brand_id', 'description', 'category_id', 'images'])

    quantity = fields.Integer(required=True)
    product = fields.Nested(ProductSchema(exclude=excluded_fields))
