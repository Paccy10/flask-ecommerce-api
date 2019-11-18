""" Module for category mocking data """

VALID_CATEGORY = {
    'name': 'cups',
    'description': 'Drinking cups'
}

INVALID_CATEGORY_WITHOUT_NAME = {
    'name': '',
    'description': ''
}

INVALID_CATEGORY_WITH_EXISTING_NAME = {
    'name': 'laptops',
    'description': ''
}

INVALID_CATEGORY_WITH_UNEXISTING_PARENT_ID = {
    'name': 'cars',
    'description': '',
    'parent_id': 3
}

UPDATED_VALID_CATEGORY = {
    'name': 'red cups',
    'description': 'Drinking red cups'
}

UPDATED_CATEGORY_WITH_EXISTING_NAME = {
    'name': 'cars',
    'description': ''
}
