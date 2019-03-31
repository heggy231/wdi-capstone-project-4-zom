from flask_wtf import FlaskForm as Form 
from models import User

from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp,                                       ValidationError, Email,                                     Length, EqualTo)


class RegisterForm(Form):
  email = StringField(
    'Email',
    validators=[
      DataRequired(),
      Email(),
      email_exists
    ])
  password = PasswordField(
    'Password',
    validators=[
      DataRequired(),
      Length(min=2),
      EqualTo('password2', message='Passwords must match')
    ])
  password2 = PasswordField(
    'Confirm Password',
    validators=[DataRequired()]
  )

  