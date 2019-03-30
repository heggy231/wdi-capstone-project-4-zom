from flask import Flask, g
from flask import render_template, flash, redirect, url_for
import json

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'heggy.secrete.key.asd'

@app.route('/')
def index():
  return render_template('Hello')

if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)