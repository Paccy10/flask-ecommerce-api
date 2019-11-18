""" Module for Server configuration """

from flask import Flask, Blueprint
from flask_restplus import Api
from flask_mail import Mail
from config.environment import AppConfig

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api/v1')
authorizations = {
    'Token Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    api_blueprint,
    title='Arrows Shop API',
    description='Online shopping API',
    security='Token Auth',
    doc='/documentation',
    authorizations=authorizations)


def create_app(config=AppConfig):
    """ Create the flask application """

    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config)
    app.register_blueprint(api_blueprint)

    return app


application = create_app()
mail = Mail(application)
