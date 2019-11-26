""" Module for product validators """

import numbers
from flask import request
from api.models.product import Product
from api.models.category import Category
from api.models.brand import Brand
from . import raise_validation_error, is_positive_integer


class ProductValidators:
    """ Product validators class """

    @classmethod
    def validate_name(cls, name, product_id=None):
        """
            Checks if the provided name doesn't exist

            Args:
                name (str): product name
            Raises:
                (ValidationError): raises an exception if the name already exists in the database
        """

        if not name or not name.strip():
            raise_validation_error(
                'The product name is required')

        product = Product.query.filter(
            Product.name == name.lower().strip()).first()

        if product:
            if request.method == 'PUT':
                if product_id != product.id:
                    raise_validation_error(
                        'The product name provided already exists')
            else:
                raise_validation_error(
                    'The product name provided already exists')

    @classmethod
    def validate_image(cls, image):
        """
            Checks if the provided image has a url and a public ID

            Args:
                image (str): product image
            Raises:
                (ValidationError): raises an exception if the image does\
                     not have a url or a public ID
        """

        if not isinstance(image, dict):
            raise_validation_error(
                'The image must be an object which has a url and a public_id')

        if not image.get('url') or not image.get('public_id')\
                or len(image.get('url').strip()) < 1\
                or len(image.get('url').strip()) < 1:
            raise_validation_error(
                'The image should have a url and a public_id')

    @classmethod
    def validate_main_image(cls, image):
        """
            validates the main image
        """
        if image is None:
            raise_validation_error('The product main image is required')

        if request.method == 'PUT':
            if image:
                cls.validate_image(image)

        else:
            cls.validate_image(image)

    @classmethod
    def validate_other_images(cls, images):
        """
            validates the other images
        """

        if images and len(images) > 0:
            for image in images:
                cls.validate_image(image)

    @classmethod
    def validate_category(cls, category_id):
        """
        Checks if the provided category ID is valid

        Args:
            category_id (int): category ID
        Raises:
            (ValidationError): raise an exception if the category ID doesn't exist in the database
        """

        if not category_id:
            raise_validation_error(
                'The category ID is required')

        if not is_positive_integer(category_id):
            raise_validation_error(
                'The category ID should be a positive integer')

        if not Category.find_by_id(category_id):
            raise_validation_error('The category ID provided doesn\'t exist')

    @classmethod
    def validate_brand(cls, brand_id):
        """
        Checks if the provided brand ID is valid

        Args:
            brand_id (int): brand ID
        Raises:
            (ValidationError): raise an exception if the brand ID doesn't exist in the database
        """

        if brand_id is not None:
            if not is_positive_integer(brand_id):
                raise_validation_error(
                    'The brand ID should be a positive integer')

            if not Brand.find_by_id(brand_id):
                raise_validation_error(
                    'The brand ID provided doesn\'t exist')

    @classmethod
    def validate(cls, data: dict, product_id=None):
        """ Validates the product """

        name = data.get('name')
        main_image = data.get('main_image')
        images = data.get('images')
        category_id = data.get('category_id')
        brand_id = data.get('brand_id')
        price = data.get('price')
        quantity = data.get('quantity')

        print(brand_id)

        cls.validate_name(name, product_id)
        cls.validate_main_image(main_image)
        cls.validate_other_images(images)
        cls.validate_category(category_id)
        cls.validate_brand(brand_id)

        if price is None:
            raise_validation_error('The price is required')

        if not isinstance(price, numbers.Number) or price < 0:
            raise_validation_error('The price must be a positive number')

        if quantity is None:
            raise_validation_error('The quantity is required')

        if not is_positive_integer(quantity):
            raise_validation_error('The quantity must be a positive integer')
