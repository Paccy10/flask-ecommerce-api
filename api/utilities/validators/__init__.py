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


def is_positive_integer(value):
    """
    Checks if the provided value is a positive integer

    Args:
        value (int): value to validate
    Raises:
        (ValidationError): raise an exception if the provided value is not a positive integer
    """

    if isinstance(value, int) and value > 0:
        return True
    else:
        return False
