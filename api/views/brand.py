""" Module for brands endpoints """

from flask import request
from flask_restplus import Resource
from api.models.brand import Brand
from api.schemas.brand import BrandSchema
from api.middlewares.permission_required import permission_required
from api.middlewares.token_required import token_required
from api.utilities.helpers.swagger.collections import brand_namespace
from api.utilities.helpers.swagger.models.brand import brand_model
from api.utilities.validators.brand import BrandValidators
from api.utilities.helpers.responses import success_response, error_response
from api.utilities.helpers import request_data_strip


@brand_namespace.route('')
class BrandResource(Resource):
    """" Resource class for brand endpoints """

    @token_required
    @permission_required
    @brand_namespace.expect(brand_model)
    def post(self):
        """ Endpoint to create the brand """

        request_data = request.get_json()
        BrandValidators.validate(request_data)

        request_data = request_data_strip(request_data)
        request_data['name'] = request_data['name'].lower()

        new_brand = Brand(**request_data)
        new_brand.save()

        brand_schema = BrandSchema()
        brand_data = brand_schema.dump(new_brand)

        success_response['message'] = 'Brand successfully created'
        success_response['data'] = {
            'brand': brand_data
        }

        return success_response, 201

#     def get(self):
#         """ Endpoint to get all categories """

#         categories_schema = CategorySchema(many=True)
#         categories = categories_schema.dump(
#             Category.query.all())

#         success_response['message'] = 'Categories successfully fetched'
#         success_response['data'] = {
#             'categories': categories
#         }

#         return success_response, 200


# @category_namespace.route('/<int:category_id>')
# class SingleCategoryResource(Resource):
#     """" Resource class for single category endpoints """

#     def get(self, category_id):
#         """"Endpoint to get a single category """

#         category_schema = CategorySchema()
#         category = category_schema.dump(Category.find_by_id(category_id))

#         if not category:
#             error_response['message'] = 'Category not found'
#             return error_response, 404
#         success_response['message'] = 'Category successfully fetched'
#         success_response['data'] = {
#             'category': category
#         }

#         return success_response, 200

#     @token_required
#     @permission_required
#     @category_namespace.expect(category_model)
#     def put(self, category_id):
#         """"Endpoint to get a single category """

#         category_schema = CategorySchema()
#         category = Category.find_by_id(category_id)

#         if not category:
#             error_response['message'] = 'Category not found'
#             return error_response, 404

#         request_data = request.get_json()
#         CategoryValidators.validate(request_data, category_id=category_id)
#         request_data = request_data_strip(request_data)
#         request_data['name'] = request_data['name'].lower()

#         category.update(request_data)

#         success_response['message'] = 'Category successfully updated'
#         success_response['data'] = {
#             'category': category_schema.dump(category)
#         }

#         return success_response, 200

#     @token_required
#     @permission_required
#     def delete(self, category_id):
#         """"Endpoint to delete a category """

#         category_schema = CategorySchema()
#         category = Category.find_by_id(category_id)

#         if not category:
#             error_response['message'] = 'Category not found'
#             return error_response, 404

#         category.delete()

#         success_response['message'] = 'Category successfully deleted'
#         success_response['data'] = {
#             'category': category_schema.dump(category)
#         }

#         return success_response, 200
