""" Module for generating the tokens """

import datetime
import os
import jwt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from dotenv import load_dotenv
from api.models.user import User

load_dotenv()


def generate_auth_token(user: dict):
    """
    Generates the authentication token
    Args:
        user(dict): user data

    Returns:
        token(str): Json Web Token
    """

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user': user
    }
    token = jwt.encode(
        payload,
        os.getenv('SECRET_KEY'),
        algorithm='HS256'
    )
    return token.decode('UTF-8')


def generate_user_token(user_id, expires_sec=1800):
    """
    Generates the token for the user
    Args:
        expires_sec(int): expiration time

    Returns:
        token(str): a string Token
    """
    s = Serializer(os.getenv('SECRET_KEY'), expires_sec)
    return s.dumps({'user_id': user_id}).decode('utf-8')


def verify_user_token(token):
    """
    Verifies if the user token is valid
    Args:
        token(str): user token

    Returns:
        user(User): user
    """
    s = Serializer(os.getenv('SECRET_KEY'))
    try:
        user_id = s.loads(token)['user_id']
    except:
        return None

    return User.query.get(user_id)
