""" Module for the User Schema """

from marshmallow import fields
from .base import BaseSchema


class UserSchema(BaseSchema):
    """ User Schema Class """

    firstname = fields.String(dump_only=True)
    lastname = fields.String(dump_only=True)
    email = fields.String(dump_only=True)
    password = fields.String(dump_only=True)
    is_admin = fields.Boolean(dump_only=True)
    is_activated = fields.Boolean(dump_only=True)
