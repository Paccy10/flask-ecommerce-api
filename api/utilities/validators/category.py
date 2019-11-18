""" Module for category validators """

from flask import request
from api.models.category import Category
from . import raise_validation_error


class CategoryValidators:
    """ Category validators class """

    @classmethod
    def validate_name(cls, name, category_id=None):
        """
            Checks if the provided name doesn't exist

            Args:
                name (str): category name
            Raises:
                (ValidationError): raises an exception if the name already exists in the database
        """

        category = Category.query.filter(
            Category.name == name.lower().strip()).first()

        if category:
            if request.method == 'PUT':
                if category_id != category.id:
                    raise_validation_error(
                        'The category name provided already exists')
            else:
                raise_validation_error(
                    'The category name provided already exists')

    @classmethod
    def validate(cls, data: dict, category_id=None):
        """ Validates the category """

        name = data.get('name')
        parent_id = data.get('parent_id')
        if not name or not name.strip():
            raise_validation_error('The category name is required')

        cls.validate_name(name, category_id)

        if parent_id:
            category = Category.find_by_id(parent_id)
            if not category:
                raise_validation_error(
                    'The parent category provided doesn\'t exist')
