""" Module for user mocking data """

VALID_USER = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'ndayisengacpac@gmail.com',
    'password': 'Password1234'
}

INVALID_USER_WTHOUT_FIRSTNAME = {
    'firstname': '',
    'lastname': 'Ndayisenga',
    'email': 'ndayisengacpac@gmail.com',
    'password': 'Password1234'
}

INVALID_USER_WTHOUT_LASTNAME = {
    'firstname': 'Pacifique',
    'lastname': '',
    'email': 'ndayisengacpac@gmail.com',
    'password': 'Password1234'
}

INVALID_USER_WTHOUT_EMAIL = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': '',
    'password': 'Password1234'
}

INVALID_USER_WTHOUT_PASSWORD = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'ndayisengacpac@gmail.com',
    'password': ''
}

INVALID_USER_WTH_INVALID_EMAIL = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'ndayisengacpacgmailcom',
    'password': 'Password1234'
}

INVALID_USER_WTH_INVALID_PASSWORD_LENGTH = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'pacifique.ndayisenga@andela.com',
    'password': 'Pass'
}

INVALID_USER_WTH_PASSWORD_WITHOUT_CAPITAL_LETTER = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'pacifique.ndayisenga@andela.com',
    'password': 'password1234'
}

INVALID_USER_WTH_PASSWORD_WITHOUT_SMALL_LETTER = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'ppacifique.ndayisenga@andela.com',
    'password': 'PASSWORD1234'
}

INVALID_USER_WTH_PASSWORD_WITHOUT_DIGIT = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'pacifique.ndayisenga@andela.com',
    'password': 'Password'
}

INVALID_USER_ALREADY_EXISTS = {
    'firstname': 'Pacifique',
    'lastname': 'Ndayisenga',
    'email': 'pacifiqueclement@gmail.com',
    'password': 'Password1234'
}

CORRECT_USER_LOGIN = {
    'email': 'ndayisengacpac@gmail.com',
    'password': 'Password1234'
}

INCORRECT_USER_LOGIN_WITH_INCORRECT_PASSWORD = {
    'email': 'ndayisengacpac@gmail.com',
    'password': 'Password12345'
}

INCORRECT_USER_LOGIN = {
    'email': 'pacifiqueclement@gmail.com',
    'password': 'Password1234'
}

RESET_REQUEST_USER = {
    'email': 'pacifiqueclement10@gmail.com'
}

UNEXISTED_RESET_REQUEST_USER = {
    'email': 'pacifiqueclement@gmail.com'
}

RESET_PASSWORD_NEW_PASSWORD = {
    'password': 'Password@1234'
}
