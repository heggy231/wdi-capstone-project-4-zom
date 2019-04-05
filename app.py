from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
# from werkzeug.utils import secure_filename

import os # for heroku importing
import models # gain access to our models
import datetime # import Python time userlogin time info
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

# login manager configuration create LoginManager class obj
# https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
# sets up our login for the app
login_manager.init_app(app)
# to login the user send user to route: signin
login_manager.login_view = 'signin'

@login_manager.user_loader
def load_user(userid):
  try:
    # looking up user by id in db
    return models.User.get(models.User.id == userid)
  except models.DoesNotExist:
    return None

# before_request, after_request are for connecting to db, Handle requests when the come in (before) and when they complete (after)
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

@app.route('/') # root route revert you to sigin form
def index():
  # Here we use a class of some kind to represent and validate our
  # client-side form data. For example, WTForms is a library that will
  # handle this for us, and we use a custom LoginForm to validate.
  form = forms.SigninForm()
  postform = forms.PostForm()

  return render_template('signin.html', form=form, current_user=current_user, postform=postform)

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

@app.route('/signin', methods=('GET', 'POST'))
def signin():
    form = forms.SigninForm() # send down form var to the template which requires it is added here! https://git.generalassemb.ly/sf-wdi-51/Flask-Models
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("your email or password doesn't match", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                ## creates session
                login_user(user)
                flash("You've been logged in", "success")
                return redirect(url_for('index'))
            else:
                flash("your email or password doesn't match", "error")
    return render_template('signin.html', form=form)

# logout user, redirect to landing
@app.route('/signout')
def signout():
  logout_user()
  flash("You've been logged out, Good Night", "success")
  return redirect(url_for('index'))

# create diary post, once done user is taken back to landing pg
@app.route('/post', methods=['GET', 'POST'])
@app.route('/post/<id>', methods=['GET', 'POST'])
def post(id=None):
  form = forms.PostForm() # send down form var to the template which requires it is added here
  if form.validate_on_submit():
    models.Post.create(
      user=g.user._get_current_object(),
      title=form.title.data,
      content=form.content.data,
    )
  return redirect(url_for('index'))

if __name__ == '__main__':
  models.initialize() # before our app runs we initialize a connection to the models
  app.run(debug=DEBUG, port=PORT)