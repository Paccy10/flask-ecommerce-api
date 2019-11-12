""" Module for the application configurations """
from os import getenv
import sys
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """ App base configuration """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = getenv('MAIL_PORT')
    MAIL_USE_TLS = getenv('MAIL_USE_TLS')
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')


class DevelopmentConfig(Config):
    """ App Development configuration """

    PORT = 5000
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')


class TestingConfig(Config):
    """ App testing configuration """

    PORT = 4000
    SQLALCHEMY_DATABASE_URI = getenv('TEST_DATABASE_URL')
    FLASK_ENV = 'testing'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}

AppConfig = TestingConfig if 'pytest' in sys.modules else config.get(
    getenv('FLASK_ENV'), 'development')
