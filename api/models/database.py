""" Module for initiliazing the database """

from flask_sqlalchemy import SQLAlchemy
from config.server import application

# Init Database
db = SQLAlchemy(application)
