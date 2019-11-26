""" Module for product fixtures """

import pytest
from api.models.product import Product


@pytest.fixture(scope='module')
def new_product(init_db, new_category, new_brand):
    """ New product fixture """
    new_category.save()
    new_brand.save()
    return Product(
        name='iphone',
        description='Apple phone',
        main_image={
            'url': 'http://someimage.url',
            'public_id': 'image_public_id'
        },
        category_id=new_category.id,
        brand_id=new_brand.id,
        price=200000,
        quantity=50
    )
