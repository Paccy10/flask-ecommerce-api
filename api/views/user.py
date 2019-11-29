""" Module for users endpoints """

from flask import request
from flask_restplus import Resource
import bcrypt
from api.utilities.helpers import request_data_strip
from api.utilities.helpers.swagger.collections import user_namespace
from api.utilities.helpers.swagger.models.user import (
    signup_model, login_model, reset_request_model, reset_password_model)
from api.utilities.helpers.responses import success_response, error_response
from api.utilities.validators.user import UserValidators
from api.utilities.generate_token import generate_auth_token, verify_user_token
from api.utilities.send_email import send_email
from api.models.user import User
from api.models.cart import Cart
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

        user_schema = UserSchema()
        user_data = user_schema.dump(new_user)

        send_email(user_data, 'Confirmation Email', 'confirmation_email.html')

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

        if user.is_activated:
            error_response['message'] = 'User account already activated'
            return error_response, 400

        user.update({'is_activated': True})
        user_cart = Cart(user_id=user.id)
        user_cart.save()

        return {
            'status': 'success',
            'message': 'User successfully activated'
        }, 200


@user_namespace.route('/login')
class UserLoginResource(Resource):
    """" Resource class for user login endpoint """

    @user_namespace.expect(login_model)
    def post(self):
        """ Endpoint to login the user """

        request_data = request.get_json()
        email = request_data['email']
        password = bytes(request_data['password'], encoding='utf-8')
        user = User.query.filter(
            User.email == email, User.is_activated).first()
        error_response['message'] = 'Incorrect username or password'
        user_schema = UserSchema()

        if user:
            user_data = user_schema.dump(user)
            hashed = bytes(user_data['password'], encoding='utf-8')

            if bcrypt.checkpw(password, hashed):
                user_schema = UserSchema(exclude=['password'])
                logged_in_user = user_schema.dump(user)
                token = generate_auth_token(logged_in_user)
                success_response['message'] = 'User successfully logged in'
                success_response['data'] = {
                    'token': token,
                    'user': logged_in_user
                }

                return success_response, 200
            return error_response, 404
        return error_response, 404


@user_namespace.route('/reset-password')
class ResetRequestResource(Resource):
    """" Resource class for user password reset request """

    @user_namespace.expect(reset_request_model)
    def post(self):
        """ Endpoint to request password reset link """

        request_data = request.get_json()
        email = request_data['email']
        user = User.find_by_email(email)

        if not user:
            error_response['message'] = 'User not found'
            return error_response, 404

        user_schema = UserSchema()
        send_email(user_schema.dump(user), 'Password Reset Request',
                   'password_reset_email.html')

        return {
            'status': 'success',
            'message': 'Request successfully submitted. Please check your email to continue.'
        }, 200


@user_namespace.route('/reset-password/<string:token>')
class PasswordResetResource(Resource):
    """" Resource class for user password reset """

    @user_namespace.expect(reset_password_model)
    def patch(self, token):
        """ Endpoint to rest user password """

        user = verify_user_token(token)

        if not user:
            error_response['message'] = 'Password reset token is invalid'
            return error_response, 400

        request_data = request.get_json()
        UserValidators.validate_password(request_data['password'])
        request_data = request_data_strip(request_data)
        bytes_password = bytes(request_data['password'], encoding='utf-8')
        hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt(10))
        password = hashed.decode('utf-8')

        user.update({'password': password})

        return {
            'status': 'success',
            'message': 'User password successfully changed'
        }, 200
