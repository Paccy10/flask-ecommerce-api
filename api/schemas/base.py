""" Module for the Base Schema """

from marshmallow import Schema, fields


class BaseSchema(Schema):
    """ Base Schema Class """

    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
    deleted = fields.Boolean(dump_only=True)
