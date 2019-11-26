""" Module for the Brand Schema """

from marshmallow import fields
from api.utilities.helpers.constants import EXCLUDED_FIELDS
from .product import ProductSchema
from .base import BaseSchema


class BrandSchema(BaseSchema):
    """ Brand Schema Class """

    name = fields.String(required=True)
    description = fields.String(required=True)
    products = fields.Nested(ProductSchema(many=True, exclude=EXCLUDED_FIELDS))
