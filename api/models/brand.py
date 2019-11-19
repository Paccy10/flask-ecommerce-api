""" Module for Brand Model """

from .database import db
from .base import BaseModel


class Brand(BaseModel):
    """ Brand Model class """

    __tablename__ = 'brands'

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
