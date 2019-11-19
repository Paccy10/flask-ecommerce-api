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

    def get(self):
        """ Endpoint to get all brands """

        brands_schema = BrandSchema(many=True)
        brands = brands_schema.dump(
            Brand.query.all())

        success_response['message'] = 'Brands successfully fetched'
        success_response['data'] = {
            'brands': brands
        }

        return success_response, 200


@brand_namespace.route('/<int:brand_id>')
class SingleBrandResource(Resource):
    """" Resource class for single brand endpoints """

    def get(self, brand_id):
        """" Endpoint to get a single brand """

        brand_schema = BrandSchema()
        brand = brand_schema.dump(Brand.find_by_id(brand_id))

        if not brand:
            error_response['message'] = 'Brand not found'
            return error_response, 404

        success_response['message'] = 'Brand successfully fetched'
        success_response['data'] = {
            'brand': brand
        }

        return success_response, 200

    @token_required
    @permission_required
    @brand_namespace.expect(brand_model)
    def put(self, brand_id):
        """" Endpoint to update brand """

        brand_schema = BrandSchema()
        brand = Brand.find_by_id(brand_id)

        if not brand:
            error_response['message'] = 'Brand not found'
            return error_response, 404

        request_data = request.get_json()
        BrandValidators.validate(request_data, brand_id=brand_id)
        request_data = request_data_strip(request_data)
        request_data['name'] = request_data['name'].lower()

        brand.update(request_data)

        success_response['message'] = 'Brand successfully updated'
        success_response['data'] = {
            'brand': brand_schema.dump(brand)
        }

        return success_response, 200

    @token_required
    @permission_required
    def delete(self, brand_id):
        """" Endpoint to delete a brand """

        brand_schema = BrandSchema()
        brand = Brand.find_by_id(brand_id)

        if not brand:
            error_response['message'] = 'Brand not found'
            return error_response, 404

        brand.delete()

        success_response['message'] = 'Brand successfully deleted'
        success_response['data'] = {
            'brand': brand_schema.dump(brand)
        }

        return success_response, 200
