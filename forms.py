# forms.py defines class to represent our form.  Add the field we need which will eventually be used with a form builder on the front end https://git.generalassemb.ly/sf-wdi-51/Flask-Models
# import the tools, fields we need
from flask_wtf import FlaskForm as Form 
# from models import User

from wtforms import StringField, PasswordField, TextAreaField, TextField, SubmitField
from wtforms.validators import (DataRequired, Regexp,                                       ValidationError, Email,                                     Length, EqualTo)
from models import User
from models import Post

def email_exists(form, field):
  if User.select().where(User.email == field.data).exists():
    raise ValidationError('Oops!! User with that email already exists.')
  return

# create the class and variable to house Field definitions
class RegisterForm(Form): # pass Form class obj to inherits WTForm field like StringField(), PasswordField()
  email = StringField( # function I am bringing in from WTF
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
      EqualTo(
        'password2', 
        message='Passwords must match')
    ])
  password2 = PasswordField(
    'Confirm Password',
    validators=[DataRequired()]
  )

# We are passing WTF Form Super class so it knows to get the functions from WTF form (Inheritance)
class SigninForm(Form):
  email = StringField(
    'Email', 
    validators=[
      DataRequired(), 
      Email()
    ])
  password = PasswordField(
    'Password', 
    validators=[
      DataRequired()
    ])

class PostForm(Form): #pass in Form class obj to inherit StringField() method and TextField
  title = StringField(
    'Title', 
    validators=[
      DataRequired()
    ])
  content = TextAreaField(
    'Tell your story...', 
    validators=[
      DataRequired()
    ])