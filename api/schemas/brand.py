""" Module for the Brand Schema """

from marshmallow import fields
from .base import BaseSchema


class BrandSchema(BaseSchema):
    """ Brand Schema Class """

    name = fields.String(dump_only=True)
    description = fields.String(dump_only=True)
