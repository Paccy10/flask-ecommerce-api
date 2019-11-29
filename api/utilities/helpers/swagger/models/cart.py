""" Module for Swagger cart models """

from flask_restplus import fields
from ..collections import (user_namespace)

cart_item_model = user_namespace.model('CartItem', {
    'product_id': fields.Integer(required=True, description='Product ID'),
    'quantity': fields.Integer(required=True, description='Product quantity', default=0)
})
