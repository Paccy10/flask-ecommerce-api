""" Module for Swagger models """

from flask_restplus import fields
from .collections import (user_namespace)

signup_model = user_namespace.model('Signup', {
    'firstname': fields.String(required=True, description='User firstname'),
    'lastname': fields.String(required=True, description='User lastname'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})
