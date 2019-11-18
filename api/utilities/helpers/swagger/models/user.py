""" Module for Swagger user models """

from flask_restplus import fields
from ..collections import (user_namespace)

signup_model = user_namespace.model('Signup', {
    'firstname': fields.String(required=True, description='User firstname'),
    'lastname': fields.String(required=True, description='User lastname'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

login_model = user_namespace.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

reset_request_model = user_namespace.model('Password Reset Request', {
    'email': fields.String(required=True, description='User email')
})

reset_password_model = user_namespace.model('Password Reset', {
    'password': fields.String(required=True, description='User new password')
})
