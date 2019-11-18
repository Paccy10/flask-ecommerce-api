""" Module for the Category Schema """

from marshmallow import fields
from .base import BaseSchema


class CategorySchema(BaseSchema):
    """ Category Schema Class """

    name = fields.String(dump_only=True)
    description = fields.String(dump_only=True)
    parent_id = fields.Integer(dump_only=True)
