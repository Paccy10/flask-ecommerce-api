""" Module for the Product Schema """

from marshmallow import fields
from .base import BaseSchema


class ProductSchema(BaseSchema):
    """ Product Schema Class """

    name = fields.String(required=True)
    description = fields.String(required=True)
    main_image = fields.Dict(required=True)
    images = fields.List(fields.Dict(), required=False)
    category_id = fields.Integer(required=True)
    brand_id = fields.Integer(required=True)
    price = fields.Decimal(required=True, as_string=True)
    quantity = fields.Integer(required=True)
