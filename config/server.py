from flask import Flask, Blueprint
from flask_restplus import Api
from config.environment import environment

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
    title='E-Commerce API',
    description='Online shopping API',
    security='Token Auth',
    doc=environment['swagger-url'],
    authorizations=authorizations)


def create_app():
    application = Flask(__name__)
    application.register_blueprint(api_blueprint)

    return application


application = create_app()
