""" Module for brand validators """

from flask import request
from api.models.brand import Brand
from . import raise_validation_error


class BrandValidators:
    """ Brand validators class """

    @classmethod
    def validate_name(cls, name, brand_id=None):
        """
            Checks if the provided name doesn't exist

            Args:
                name (str): brand name
            Raises:
                (ValidationError): raises an exception if the name already exists in the database
        """

        brand = Brand.query.filter(Brand.name == name.lower().strip()).first()

        if brand:
            if request.method == 'PUT':
                if brand_id != brand.id:
                    raise_validation_error(
                        'The brand name provided already exists')
            else:
                raise_validation_error(
                    'The brand name provided already exists')

    @classmethod
    def validate(cls, data: dict, brand_id=None):
        """ Validates the brand """

        name = data.get('name')

        if not name or not name.strip():
            raise_validation_error('The brand name is required')

        cls.validate_name(name, brand_id)
