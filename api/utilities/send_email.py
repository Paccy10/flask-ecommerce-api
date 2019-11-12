""" Module for sending emails """

from flask import render_template
from flask_mail import Message
from config.server import mail
from flask import url_for
from .generate_token import generate_user_token


def send_confirmation_email(user):
    """ Send confirmation email function """

    token = generate_user_token(user['id'])
    msg = Message('Confirmation Email',
                  sender=('Arrows Shop', 'info.arrows2019@gmail.com'), recipients=[user['email']])
    msg.html = render_template(
        'confirmation_email.html', user=user, token=token)

    mail.send(msg)
