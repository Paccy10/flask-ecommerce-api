"""" Module for common validators """

from werkzeug.exceptions import BadRequest


def raise_validation_error(message):
    """
    Raises validation error

    Args:
        message (str): error message
    Raises:
        (ValidationError): raise an exception
    """

    error = BadRequest()
    error.data = {
        'status': 'error',
        'message': message
    }
    raise error


# def is_empty(string):
#     """
#     Checks if the provided field is empty

#     Args:
#         string (str): string to validate
#     Raises:
#         (ValidationError): raise an exception for each field that is empty
#     """

#     for field in fields:
#         if not field or not field.strip():
#             raise_validation_error(f'The {field} is required')
