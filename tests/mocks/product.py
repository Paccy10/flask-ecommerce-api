""" Module for product mocking data """

VALID_PRODUCT = {
    'name': 'samsung galaxy j5 prime',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITHOUT_NAME = {
    'name': '',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_EXISTING_NAME = {
    'name': 'iphone',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITHOUT_IMAGE = {
    'name': 'motorola',
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_STRING_IMAGE = {
    'name': 'motorola',
    'main_image': 'image',
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_INVALID_IMAGE = {
    'name': 'motorola',
    'main_image': {},
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_INVALID_OTHER_IMAGES = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'images': ['image1', 'image2'],
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITHOUT_CATEGORY_ID = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_INVALID_CATEGORY_ID = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': '1',
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_UNEXISTED_CATEGORY_ID = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 10,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_INVALID_BRAND_ID = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': '1',
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITH_UNEXISTED_BRAND_ID = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 10,
    'price': 200000,
    'quantity': 50
}

INVALID_PRODUCT_WITHOUT_PRICE = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'quantity': 50
}

INVALID_PRODUCT_WITH_INVALID_PRICE = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': '200000',
    'quantity': 50
}

INVALID_PRODUCT_WITHOUT_QUANTITY = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': 200000
}

INVALID_PRODUCT_WITH_INVALID_QUANTITY = {
    'name': 'motorola',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': '50'
}

UPDATED_VALID_PRODUCT = {
    'name': 'iphone',
    'main_image': {
        'url': 'http://someimage.url',
        'public_id': 'image_public_id'
    },
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}

UPDATED_INVALID_PRODUCT_WITH_EXISTED_NAME = {
    'name': 'iphone',
    'category_id': 1,
    'brand_id': 1,
    'price': 200000,
    'quantity': 50
}
