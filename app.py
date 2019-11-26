""" Main application module """

from flask_migrate import Migrate
from config.server import application
from api.models.database import db
from api.models.user import User
from api.models.category import Category
from api.models.brand import Brand
from api.models.product import Product
import api.views.user
import api.views.category
import api.views.brand
import api.views.product

migrate = Migrate(application, db)


@application.errorhandler(404)
def page_not_found(e):
    """ Page not found error handling """

    return {
        'status': 'error',
        'message': 'Undefined route'
    }, 404


if __name__ == '__main__':
    application.run()
