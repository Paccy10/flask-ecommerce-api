""" Module for Cart Model """

from .database import db
from .base import BaseModel


class Cart(BaseModel):
    """ Cart Model class """

    __tablename__ = 'carts'

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), unique=True, nullable=False)
    owner = db.relationship('User', backref='owner', lazy='joined')
    items = db.relationship('CartItem', backref='items', lazy='joined')
