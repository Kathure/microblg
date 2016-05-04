#!/usr/bin/python

from flask.ext.wtf import Form #imports Form class
from wtforms import StringField, BooleanField #imports field classes we need
from wtforms.validators import DataRequired #imports a validator

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
