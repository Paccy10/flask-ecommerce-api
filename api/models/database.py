""" Module for initiliazing the database """

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config.server import application

load_dotenv()

# Init Database
db = SQLAlchemy(application)
