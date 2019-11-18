""" Module for categories endpoints """

from flask import request
from flask_restplus import Resource
from api.models.category import Category
from api.schemas.category import CategorySchema
from api.middlewares.permission_required import permission_required
from api.middlewares.token_required import token_required
from api.utilities.helpers.swagger.collections import category_namespace
from api.utilities.helpers.swagger.models.category import category_model
from api.utilities.validators.category import CategoryValidators
from api.utilities.helpers.constants import EXCLUDED_FIELDS
from api.utilities.helpers.responses import success_response, error_response
from api.utilities.helpers import request_data_strip


@category_namespace.route('')
class CategoryResource(Resource):
    """" Resource class for category endpoints """

    @token_required
    @permission_required
    @category_namespace.expect(category_model)
    def post(self):
        """ Endpoint to create the category """

        request_data = request.get_json()
        CategoryValidators.validate(request_data)

        request_data = request_data_strip(request_data)
        request_data['name'] = request_data['name'].lower()
        new_category = Category(**request_data)
        new_category.save()

        category_schema = CategorySchema(exclude=EXCLUDED_FIELDS)
        category_data = category_schema.dump(new_category)

        success_response['message'] = 'Category successfully created'
        success_response['data'] = {
            'category': category_data
        }

        return success_response, 201

    def get(self):
        """ Endpoint to get all categories """

        categories_schema = CategorySchema(many=True, exclude=EXCLUDED_FIELDS)
        categories = categories_schema.dump(
            Category.query.filter_by(deleted=False))

        success_response['message'] = 'Categories successfully fetched'
        success_response['data'] = {
            'categories': categories
        }

        return success_response, 200


@category_namespace.route('/<int:category_id>')
class SingleCategoryResource(Resource):
    """" Resource class for single category endpoints """

    def get(self, category_id):
        """"Endpoint to get a single category """

        category_schema = CategorySchema(exclude=EXCLUDED_FIELDS)
        category = category_schema.dump(Category.find_by_id(category_id))

        if not category:
            error_response['message'] = 'Category not found'
            return error_response, 404
        success_response['message'] = 'Category successfully fetched'
        success_response['data'] = {
            'category': category
        }

        return success_response, 200
