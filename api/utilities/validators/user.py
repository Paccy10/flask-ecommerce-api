""" Module for user validators """

import re
from api.models.user import User
from . import raise_validation_error


class UserValidators:
    """ User validators class """

    @classmethod
    def validate_email(cls, email):
        """
        Checks if the provided email is valid

        Args:
            email (str): user email
        Raises:
            (ValidationError): raise an exception if the email pattern doesn't
            correspond the provided email regex or if the email already exists in the database
        """

        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email.strip()):
            raise_validation_error('The email provided is not valid')

        if User.query.filter(User.email == email.strip(), User.deleted.is_(False)).first():
            raise_validation_error('The email provided already exists')

    @classmethod
    def validate_password(cls, password):
        """
        Checks if the provided password is strong

        Args:
            password (str): user password
        Raises:
            (ValidationError): raise an exception if the password doesn't
            contain an uppercase letter, a lowercase letter, a digit or if
            the password length is less than 8
        """
        if len(password) < 8:
            raise_validation_error(
                'The password must be at least 8 characters')

        if not any(char.isupper() for char in password):
            raise_validation_error(
                'The password must have at least one uppercase letter')

        if not any(char.islower() for char in password):
            raise_validation_error(
                'The password must have at least one lowercase letter')

        if not any(char.isdigit() for char in password):
            raise_validation_error(
                'The password must have at least one digit')

    @classmethod
    def validate(cls, data: dict):
        """ Validates the user """

        for key, value in data.items():
            if not value or not value.strip():
                raise_validation_error(f'The {key} is required')

        cls.validate_email(data.get('email'))
        cls.validate_password(data.get('password'))
