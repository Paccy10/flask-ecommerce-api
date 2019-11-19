""" Module for brand mocking data """

VALID_BRAND = {
    'name': 'adidas',
    'description': ''
}

INVALID_BRAND_WITHOUT_NAME = {
    'name': '',
    'description': ''
}

INVALID_BRAND_WITH_EXISTING_NAME = {
    'name': 'nike',
    'description': ''
}


UPDATED_VALID_BRAND = {
    'name': 'nike',
    'description': 'Nike, Inc. is an American multinational corporation\
         that is engaged in the design, development, manufacturing, and\
         worldwide marketing and sales of footwear, apparel, equipment, \
        accessories, and services. '
}

UPDATED_BRAND_WITH_EXISTING_NAME = {
    'name': 'puma',
    'description': ''
}
