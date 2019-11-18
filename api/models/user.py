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

    @classmethod
    def find_by_email(cls, user_email):
        """ Finds a user instance by email """

        user = cls.query.filter_by(
            email=user_email, is_activated=True).first()
        if user:
            return user
        return None
