""" Module for user mocking data """

VALID_USER = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "ndayisengacpac@gmail.com",
    "password": "Password1234"
}

INVALID_USER_WTHOUT_FIRSTNAME = {
    "firstname": "",
    "lastname": "Ndayisenga",
    "email": "ndayisengacpac@gmail.com",
    "password": "Password1234"
}

INVALID_USER_WTHOUT_LASTNAME = {
    "firstname": "Pacifique",
    "lastname": "",
    "email": "ndayisengacpac@gmail.com",
    "password": "Password1234"
}

INVALID_USER_WTHOUT_EMAIL = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "",
    "password": "Password1234"
}

INVALID_USER_WTHOUT_PASSWORD = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "ndayisengacpac@gmail.com",
    "password": ""
}

INVALID_USER_WTH_INVALID_EMAIL = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "ndayisengacpacgmailcom",
    "password": "Password1234"
}

INVALID_USER_WTH_INVALID_PASSWORD_LENGTH = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "pacifiqueclement@gmail.com",
    "password": "Pass"
}

INVALID_USER_WTH_PASSWORD_WITHOUT_CAPITAL_LETTER = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "pacifiqueclement@gmail.com",
    "password": "password1234"
}

INVALID_USER_WTH_PASSWORD_WITHOUT_SMALL_LETTER = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "pacifiqueclement@gmail.com",
    "password": "PASSWORD1234"
}

INVALID_USER_WTH_PASSWORD_WITHOUT_DIGIT = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "pacifiqueclement@gmail.com",
    "password": "Password"
}

INVALID_USER_ALREADY_EXISTS = {
    "firstname": "Pacifique",
    "lastname": "Ndayisenga",
    "email": "pacifique.ndayisenga@andela.com",
    "password": "Password1234"
}
