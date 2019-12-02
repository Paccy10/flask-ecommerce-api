""" Module for cart endpoints """

from flask import request
from flask_restplus import Resource
from api.models.cart import Cart
from api.models.product import Product
from api.models.cart_item import CartItem
from api.schemas.cart import CartSchema
from api.middlewares.token_required import token_required
from api.utilities.helpers.swagger.collections import user_namespace
from api.utilities.helpers.swagger.models.cart import cart_item_model
from api.utilities.helpers.responses import success_response, error_response
from api.utilities.helpers import request_data_strip
from api.utilities.helpers.constants import EXCLUDED_FIELDS
from api.utilities.validators.cart import CartValidators


@user_namespace.route('/cart')
class SingleCartResource(Resource):
    """" Resource class for single cart endpoints """

    @token_required
    def get(self):
        """ Endpoint to get user cart """

        cart_schema = CartSchema(exclude=EXCLUDED_FIELDS)
        user_id = request.decoded_token['user']['id']
        cart = Cart.query.filter_by(user_id=user_id).first()
        cart_data = cart_schema.dump(cart)

        success_response['message'] = 'Cart successfully fetched'
        success_response['data'] = {
            'cart': cart_data
        }

        return success_response, 200

    @token_required
    @user_namespace.expect(cart_item_model)
    def post(self):
        """ Endpoint to add items to cart """

        request_data = request.get_json()
        CartValidators.validate_item(request_data)
        request_data = request_data_strip(request_data)

        user_id = request.decoded_token['user']['id']
        cart = Cart.query.filter_by(user_id=user_id).first()
        request_data.update({'cart_id': cart.id})
        cart_item = CartItem.query.filter_by(
            cart_id=cart.id, product_id=request_data['product_id']).first()
        product = Product.find_by_id(request_data['product_id'])

        if cart_item:
            updated_quantity = product.quantity - request_data['quantity']
            request_data['quantity'] += cart_item.quantity
            CartValidators.validate_item(request_data)
            cart_item.update(request_data)
            product.update({'quantity': updated_quantity})

        else:
            new_cart_item = CartItem(**request_data)
            new_cart_item.save()
            new_quantity = product.quantity - request_data['quantity']
            product.update({'quantity': new_quantity})

        cart_schema = CartSchema(exclude=EXCLUDED_FIELDS)
        success_response['message'] = 'Item successfully added to the cart'
        success_response['data'] = {
            'cart': cart_schema.dump(cart)
        }

        return success_response, 200


@user_namespace.route('/cart/items/<int:cart_item_id>')
class SingleCartItemResource(Resource):
    """" Resource class for single cart item endpoints """

    @token_required
    def delete(self, cart_item_id):
        """" Endpoint to remove an item from the cart """

        cart_schema = CartSchema(exclude=EXCLUDED_FIELDS)
        user_id = request.decoded_token['user']['id']
        cart = Cart.query.filter_by(user_id=user_id).first()
        cart_item = CartItem.query.filter_by(
            id=cart_item_id, cart_id=cart.id).first()

        if not cart_item:
            error_response['message'] = 'Cart Item not found'
            return error_response, 404

        product = Product.find_by_id(cart_item.product_id)
        quantity = product.quantity + cart_item.quantity
        product.update({'quantity': quantity})
        cart_item.delete()

        success_response['message'] = 'Item successfully removed from the cart'
        success_response['data'] = {
            'cart': cart_schema.dump(cart)
        }

        return success_response, 200
