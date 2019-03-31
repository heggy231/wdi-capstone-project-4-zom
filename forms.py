from flask_wtf import FlaskForm as Form 
# from models import User

from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp,                                       ValidationError, Email,                                     Length, EqualTo)

def name_exists(form, field):
  # if User.select().where(User.username == field.data).exists():
  #   raise ValidationError('User with that name already exists.')
  return

def email_exists(form, field):
  # if User.select().where(User.email == field.data).exists():
  #   raise ValidationError('User with that email already exists.')
  return

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

