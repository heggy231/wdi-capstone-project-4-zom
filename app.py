from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
# from werkzeug.utils import secure_filename

import os
# import models 
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

@app.route('/')
def index():
  return render_template('landing.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
  form = forms.RegisterForm()
  return render_template('register.html', form=form)


if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)