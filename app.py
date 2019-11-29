""" Main application module """

from flask_migrate import Migrate
from config.server import application
from api.models.database import db
from api.models.user import User
from api.models.category import Category
from api.models.brand import Brand
from api.models.product import Product
from api.models.cart import Cart
from api.models.cart_item import CartItem
import api.views.user
import api.views.category
import api.views.brand
import api.views.product
import api.views.cart

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
