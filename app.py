from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
# from werkzeug.utils import secure_filename

import os
import models 
import forms

import json
# to upload photo
from flask import send_from_directory
from key_zom import key_zom


#///////////uncomment this for heroku///////////////
# from flask.ext.heroku import Heroku
# heroku = Heroku(app)

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = key_zom

# before_request, after_request are for connecting to db
@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/')
def signin():
  form = forms.SigninForm()
  return render_template('signin.html', form=form)

@app.route('/register', methods=('GET', 'POST'))
def register():
  form = forms.RegisterForm()
  if form.validate_on_submit():
    flash('Yay you registered', 'success')
    # creating the user when user first registers
    models.User.create_user(
      email=form.email.data,
      password=form.password.data
    )
  return render_template('register.html', form=form)


if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)