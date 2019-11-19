""" Module for Swagger brand models """

from flask_restplus import fields
from ..collections import (brand_namespace)

brand_model = brand_namespace.model('Brand', {
    'name': fields.String(required=True, description='Brand name'),
    'description': fields.String(required=False, description='Brand description')
})
