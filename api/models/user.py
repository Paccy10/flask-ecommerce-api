""" Module for User Model """

from .database import db
from .base import BaseModel


class User(BaseModel):
    """ User Model class """

    __tablename__ = 'users'

    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    is_activated = db.Column(db.Boolean, default=False, nullable=False)
