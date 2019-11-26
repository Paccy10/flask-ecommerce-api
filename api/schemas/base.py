""" Module for the Base Schema """

from marshmallow import Schema, fields


class BaseSchema(Schema):
    """ Base Schema Class """

    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
