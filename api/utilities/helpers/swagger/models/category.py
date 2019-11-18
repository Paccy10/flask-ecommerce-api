""" Module for Swagger category models """

from flask_restplus import fields
from ..collections import (category_namespace)

category_model = category_namespace.model('Signup', {
    'name': fields.String(required=True, description='Category name'),
    'description': fields.String(required=True, description='Category description'),
    'parent_id': fields.String(required=True, description='Category parent ID'),
})
