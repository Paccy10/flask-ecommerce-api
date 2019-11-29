""" Module for the Cart Schema """

from marshmallow import fields
from api.utilities.helpers.constants import EXCLUDED_FIELDS
from .base import BaseSchema
from .user import UserSchema
from .cart_item import CartItemSchema


class CartSchema(BaseSchema):
    """ Cart Schema Class """

    user_excluded_fields = EXCLUDED_FIELDS.copy()
    user_excluded_fields.extend(['password', 'is_admin', 'is_activated'])

    owner = fields.Nested(UserSchema(exclude=user_excluded_fields))
    items = fields.Nested(CartItemSchema(many=True, exclude=EXCLUDED_FIELDS))
