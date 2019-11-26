""" Module for Swagger product models """

from flask_restplus import fields
from ..collections import (product_namespace)

product_model = product_namespace.model('Product', {
    'name': fields.String(required=True, description='Product name'),
    'description': fields.String(required=False, description='Product description'),
    'main_image': fields.Raw(require=True, description='Product image', example={
        'public_id': 'fsfdfd',
        'url': 'http://someimage.url'
    }),
    'images': fields.List(fields.Raw(example={
        'public_id': 'fsfdfd',
        'url': 'http://someimage.url'
    }), required=False, description='Product other images'),
    'category_id': fields.Integer(required=True, description='Product category ID'),
    'brand_id': fields.Integer(required=True, description='Product brand ID'),
    'price': fields.Fixed(required=True, description='Product price'),
    'quantity': fields.Integer(required=True, description='Product quantity', default=0)
})
