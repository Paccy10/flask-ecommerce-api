""" Module for products endpoints """

from flask import request
from flask_restplus import Resource
from api.models.product import Product
from api.schemas.product import ProductSchema
from api.middlewares.permission_required import permission_required
from api.middlewares.token_required import token_required
from api.utilities.pagination_handler import paginate_resource
from api.utilities.helpers.swagger.collections import product_namespace
from api.utilities.helpers.swagger.models.product import product_model
from api.utilities.validators.product import ProductValidators
from api.utilities.helpers.responses import success_response, error_response
from api.utilities.helpers import request_data_strip


@product_namespace.route('')
class ProductResource(Resource):
    """" Resource class for product endpoints """

    @token_required
    @permission_required
    @product_namespace.expect(product_model)
    def post(self):
        """ Endpoint to create the category """

        request_data = request.get_json()
        ProductValidators.validate(request_data)

        request_data = request_data_strip(request_data)
        request_data['name'] = request_data['name'].lower()
        new_product = Product(**request_data)
        new_product.save()

        product_schema = ProductSchema()
        product_data = product_schema.dump(new_product)

        success_response['message'] = 'Product successfully created'
        success_response['data'] = {
            'product': product_data
        }
        return success_response, 201

    def get(self):
        """ Endpoint to get all products """

        products_schema = ProductSchema(many=True)
        data, meta = paginate_resource(Product, products_schema)

        success_response['message'] = 'Products successfully fetched'
        success_response['data'] = {
            'products': data,
            'meta': meta
        }

        return success_response, 200


@product_namespace.route('/<int:product_id>')
class SingleProductResource(Resource):
    """" Resource class for single product endpoints """

    def get(self, product_id):
        """" Endpoint to get a single product """

        product_schema = ProductSchema()
        product = product_schema.dump(Product.find_by_id(product_id))

        if not product:
            error_response['message'] = 'Product not found'
            return error_response, 404
        success_response['message'] = 'Product successfully fetched'
        success_response['data'] = {
            'product': product
        }

        return success_response, 200

    @token_required
    @permission_required
    @product_namespace.expect(product_model)
    def put(self, product_id):
        """" Endpoint to update product """

        product_schema = ProductSchema()
        product = Product.find_by_id(product_id)

        if not product:
            error_response['message'] = 'Product not found'
            return error_response, 404

        request_data = request.get_json()
        ProductValidators.validate(request_data, product_id=product_id)
        request_data = request_data_strip(request_data)
        request_data['name'] = request_data['name'].lower()

        product.update(request_data)

        success_response['message'] = 'Product successfully updated'
        success_response['data'] = {
            'product': product_schema.dump(product)
        }

        return success_response, 200

    @token_required
    @permission_required
    def delete(self, product_id):
        """" Endpoint to delete a product """

        product_schema = ProductSchema()
        product = Product.find_by_id(product_id)

        if not product:
            error_response['message'] = 'Product not found'
            return error_response, 404

        product.delete()

        success_response['message'] = 'Product successfully deleted'
        success_response['data'] = {
            'product': product_schema.dump(product)
        }

        return success_response, 200
