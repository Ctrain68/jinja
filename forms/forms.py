from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegistrationForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign in')
