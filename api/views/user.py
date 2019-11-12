""" Module for users endpoints """

from flask import request
from flask_restplus import Resource
import bcrypt
from api.utilities.helpers import request_data_strip
from api.utilities.helpers.swagger.collections import user_namespace
from api.utilities.helpers.swagger.models import signup_model
from api.utilities.helpers.constants import EXCLUDED_FIELDS
from api.utilities.helpers.responses import success_response, error_response
from api.utilities.validators.user import UserValidators
from api.utilities.generate_token import generate_auth_token, verify_user_token
from api.utilities.send_email import send_confirmation_email
from api.models.user import User
from api.schemas.user import UserSchema


@user_namespace.route('/signup')
class UserSignupResource(Resource):
    """" Resource class for user signup endpoint """

    @user_namespace.expect(signup_model)
    def post(self):
        """ Endpoint to create the user """

        request_data = request.get_json()
        UserValidators.validate(request_data)

        request_data = request_data_strip(request_data)

        bytes_password = bytes(request_data['password'], encoding='utf-8')
        hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt(10))
        request_data['password'] = hashed.decode('utf-8')

        new_user = User(**request_data)
        new_user.save()

        excluded = EXCLUDED_FIELDS.copy()
        user_schema = UserSchema(exclude=excluded)
        user_data = user_schema.dump(new_user)

        send_confirmation_email(user_data)

        return {
            'status': 'success',
            'message': 'User successfully created. Please check your email to continue.'
        }, 201


@user_namespace.route('/activate/<string:token>')
class UserActivateResource(Resource):
    """" Resource class for user account activation endpoint """

    def get(self, token):
        """ Endpoint to activate the user account """

        user = verify_user_token(token)
        if user is None:
            error_response['message'] = 'Account activation token is invalid'
            return error_response, 400

        user.update({'is_activated': True})

        excluded = EXCLUDED_FIELDS.copy()
        excluded.append('password')
        user_schema = UserSchema(exclude=excluded)
        user_data = user_schema.dump(user)

        token = generate_auth_token(user_data)

        success_response['message'] = 'User successfully activated'
        success_response['data'] = {
            'token': token,
            'user': user_data
        }

        return success_response, 200
