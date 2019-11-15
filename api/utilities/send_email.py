""" Module for sending emails """

from flask import render_template
from flask_mail import Message
from config.server import mail
from .generate_token import generate_user_token


def send_email(user, subject, template):
    """ Send email """

    token = generate_user_token(user['id'])
    msg = Message(subject,
                  sender=('Arrows Shop', 'info.arrows2019@gmail.com'), recipients=[user['email']])
    msg.html = render_template(template, user=user, token=token)

    mail.send(msg)
