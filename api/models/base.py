""" Module for the base Model """

import datetime
from .database import db


class BaseModel(db.Model):
    """ Base Model class """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, default=False, nullable=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def save(self):
        """ Save a model instance """

        self.created_at = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """ Update a model instance """

        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        """ Delete a model instance """

        self.deleted = True
        self.deleted_at = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, instance_id):
        """ Finds a model instance """

        instance = cls.query.filter_by(id=instance_id, deleted=False).first()
        if instance:
            return instance
        return None
