#!/usr/bin/env python
from flask import Flask, g
from flask import request, make_response, render_template, flash, redirect, url_for
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
    user = models.User.get(models.User.id == userid)
    return user
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

  # anytime user hits index we will get the time
  login_time = datetime.datetime.now()
  # Here we use a class of some kind to represent and validate our
  # client-side form data. For example, WTForms is a library that will
  # handle this for us, and we use a custom LoginForm to validate.
  form = forms.SigninForm()
  postform = forms.PostForm()

  # remember to import make_response, request from flask for cookie!
  resp = make_response(render_template('signin.html', form=form, current_user=current_user, postform=postform)) # https://stackoverflow.com/questions/46661083/how-to-set-cookie-in-python-flask, http://flask.pocoo.org/docs/1.0/api/#flask.Response.set_cookie
  resp.set_cookie('login_time', login_time.strftime('%Y-%m-%d  %I:%M%p') )
  
  return resp

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
  # update the time info when user signedin_at col to none so next time it will get the newest next login info: https://stackoverflow.com/questions/19239324/how-to-use-update-query-in-flask-peewee, Update query in Flask Peewee?
  # q = models.User.update(models.User.signedin_at = None).where(models.User.email==current_user.email) # email is unique
  # q.execute() # Will do the SQL update query.

  logout_user()
  flash("You've been logged out, Good Night", "success")
  return redirect(url_for('index'))

@app.route('/post', methods=['GET', 'POST'])
@app.route('/post/', methods=['GET', 'POST'])
@app.route('/post/<id>', methods=['GET', 'POST'])
def post(id=None):
  form = forms.PostForm()
  if form.validate_on_submit():
    models.Post.create(
      user=g.user._get_current_object(), # g.user is current_user obj, local proxy all the info about current user is under property current_user.user_get_current_object(). so remember to call the user_get_current_object() when called alone.  but when it is called with db current_user then no need to call user_get_current_object(); since db will lazy load. https://www.reddit.com/r/flask/comments/58zhae/af_current_user_vs_current_user_get_current_object/
      title=form.title.data,
      content=form.content.data,
      starttimestamp=datetime.datetime.strptime( request.cookies.get('login_time'), '%Y-%m-%d  %I:%M%p')# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior year(2019)-month-day  %I(12hrformatHour):%Minute %p(PM/AM)
    )
    return redirect(url_for('index')) # creating url > calling index function


# create diary post, once done user is taken back to landing pg
@app.route('/posts', methods=['GET', 'POST'])
@app.route('/posts/', methods=['GET', 'POST'])
@app.route('/posts/<id>', methods=['GET', 'POST'])
def posts(id=None):
  # if user just didn't click on one specific post then show the whole list of posts
  if id == None:
    # select all posts
    return render_template('posts.html', posts=g.user.posts)

  else: # called first part of editing when user clicks on edit pencil in posts.html
    post_id = int(id) #id passed in from db is string usu so go ahead and make it into integer here.
    #get query to return the right one post <id> here!
    post = models.Post.get(models.Post.id == post_id)
    return render_template('post.html', post=post) # once I got the id I then show the post.html to user for more editing

@app.route('/post/<postid>/delete')
@login_required # prevents users from deleting w/o login
def delete_post(postid):
  post_id = int(postid)
  post = models.Post.get(models.Post.id == post_id)
  post.delete_instance()
  return redirect(url_for('posts'))

@app.route('/post/<postid>/edit', methods=['GET', 'POST']) # called inside of post.html during second phase of editing logic
@login_required
def edit_post(postid):
  post_id = int(postid) # convert str to int
  post = models.Post.get(models.Post.id == post_id)

  form = forms.PostForm() # forms.py call class PostForm inherit its properties
  post.title = form.title.data # assign selected post.title tobe overwritten by form.title.data
  post.content = form.content.data # assign selected post.content tobe overwritten by form.content.data
  post.save() # http://docs.peewee-orm.com/en/latest/peewee/querying.html
  flash("Great, Your diary has been edited", "success")
  return redirect(f"/posts/{post_id}")


if __name__ == '__main__':
  models.initialize() # before our app runs we initialize a connection to the models
  app.run(debug=DEBUG, port=PORT)