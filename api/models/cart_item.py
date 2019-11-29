""" Module for Cart Items Model """

from .database import db
from .base import BaseModel


class CartItem(BaseModel):
    """ CartItem Model class """

    __tablename__ = 'cart_items'

    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product = db.relationship('Product', backref='product', lazy='joined')
