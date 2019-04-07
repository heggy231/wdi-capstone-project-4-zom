# Flask Templates!

Time to build out an app in flask!

## Initial Setup

### Virtual env

```
$ git clone git@git.generalassemb.ly:sf-wdi-51/Flask-Templates.git
$ cd Flask-Templates
```

```
$ pip3 install virtualenv
$ virtualenv .env -p python3
$ source .env/bin/activate
```

You should see `(.env)` which is virtualenvironment you just created!
<img src="https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-03-30%20at%2011.29.28%20AM.png?1553970695215">

Most of these we will be using later on with our models lesson.

### Dependencies (Building my app first time)

```bash
flask-login
flask-bcrypt
flask
peewee
flask-wtf
flask-cors  // If you are running react frontend with Flask backedn
```

```bash
$ pip3 install flask flask-login flask-bcrypt peewee flask-wtf flask-cors
$ pip3 freeze > requirements.txt
```

### How to run this app: Downloading this app from a github repo online:
> `ctrl + c` // Note: kill all python that maybe running in the background `ctrl + c`a to kill
> pip3 install virtualenv
> virtualenv .env -p python3
> source .env/bin/activate
> pip3 install -r requirements.txt
> python3 app.py
// I expect to see it running `http://localhost:8000/`


### How to run this app: You close this app and opening it second time:

> `ctrl + c`// Note: kill all python that maybe running in the background `ctrl + c`a to kill
> virtualenv .env -p python3
> source .env/bin/activate
> pip3 install -r requirements.txt
> python3 app.py
// I expect to see it running `http://localhost:8000/`


### Anytime you install new dependencies:
> pip3 freeze > requirements.txt

### The App

We are going to recreate one of my favorite websites! Reddit.

in app.py:

```py
from flask import Flask, g
from flask import render_template, flash, redirect, url_for
import json


DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

@app.route('/')
def index():
    return render_template('Hello')

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)

```

Now you can run your server with..

```bash
python3 app.py
```

Head to your browser and check it out!

Now that we have it up and running let's start making some templates.

## View Functions

Let's create the inital index view and break down the index function.

in App.js:

```py
@app.route('/')
def index():
    with open('subs.json') as json_data:
        subs = json.load(json_data)
        return render_template('subs.html', subs=subs)
```

Now we need to create a template folder and our first 2 templates.

```bash
mkdir templates && cd templates
touch layout.html subs.html
```

In layout.html:

```html
<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.css"
    />
    <link rel="stylesheet" type="text/css" href="/static/style.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>

  <body>
    <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item " href="{{url_for('index')}}">
          <img src="https://i.imgur.com/sdO8tAw.png" width="50" height="100" />
          <h3>Redd</h3>
        </a>
        <a
          role="button"
          class="navbar-burger burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            Welcome
          </a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-light" href="" title="login">Login</a>
              <a class="button is-primary" href="" title="register"
                ><strong>Sign up</strong></a
              >
            </div>
          </div>
        </div>
      </div>
    </nav>
    <br />
    <div class="columns">
      <div class="column">
        {% block content %} {% endblock %}
      </div>
      <div class="column"></div>
    </div>
  </body>
</html>
```

This is going to server as our main page as we swap between different templates. notice the **{% block content%}** section. This location is where our templates will appear.

In subs.html:

```html
{% extends "layout.html" %} {% block content %}
<h1>Subs</h1>
{% for sub in subs %}
<article class="message is-dark">
  <div class="message-header">
    <a>{{sub.name}}</a>
  </div>
  <div class="message-body">
    {{sub.description}}
  </div>
</article>
{% endfor %} {% endblock %}
```

Notice the **{% extends "layout.html" %}**? This is how we tell the templates to connect to the other file. Also let's take a look at our view function again...

```py
@app.route('/')
def index():
    with open('subs.json') as json_data:
        subs = json.load(json_data)
        return render_template('subs.html', subs=subs)
```

As you can see we have a variable called **subs**. Inside the view function we can actually send all of our "DB subreddits" to our html page. Crazy right?!

![mind blown](https://media.giphy.com/media/SDogLD4FOZMM8/giphy.gif)

So now our html can loop through our subs and create html per sub. Amazing!

But we aren't done yet...

## View Route Params

So now we can view our sub reddits, but what about individual pages? Time for params.. kinda.

Let's take a look at how this is going to work.

In app.py:

```py

@app.route('/r')
@app.route('/r/<sub>')
def r(sub=None):
    with open('subs.json') as json_data:
        subs = json.load(json_data)
        if sub == None:
            return render_template('subs.html', subs=subs)
        else:
            sub_id = int(sub)
            return render_template('sub.html', sub=subs[sub_id])

```

The same view function will activate for both routes requested.

Based inside the r route we can see the /r or /r/id. We can grab that variable through the url and use it to filter our reddits.

So now let's create a new file called sub.html

In sub.html:

```html
{% extends "layout.html" %} {% block content %}
<h1>Sub</h1>
<article class="message is-dark">
  <div class="message-header">
    <a>{{sub.name}}</a>
  </div>
  <div class="message-body">
    {{sub.description}}
  </div>
</article>
{% endblock %}
```

And now we need to link the single page to the full page in our subs.html.

```html
{% extends "layout.html" %}

{% block content %}
<h1>Subs</h1>
{% for sub in subs %}
<article class="message is-dark">
    <div class="message-header">
        <!-- this is what is new -->
        <a href={{url_for('r', sub=sub.id)}}>{{sub.name}}</a>
    </div>
    <div class="message-body">
        {{sub.description}}
    </div>
</article>
{% endfor %}
{% endblock %}
```

We added into our href the link to be created and passed the id back to our view function. With this line..

```html
<a href={{url_for('r', sub=sub.id)}}>{{sub.name}}</a>
```

Fire up that server and check it out in action!

## Activity

Now its YOUR turn to build some view function with your partner. Build out your posts and post route both extending layout content.

IF you get lost the solution code is below.. but try before you look!

**HINT**
_The functions and html will look very similar, but the posts have additional information. Check out the posts.json for the data you will be working with._

<details>
<summary>Solution</summary>
<br>
app.py

```py

@app.route('/posts')
@app.route('/posts/<id>')
def posts(id=None):
    with open('posts.json') as json_data:
        posts = json.load(json_data)
        if id == None:
            return render_template('posts.html', posts=posts)
        else:
            post_id = int(id)
            return render_template('post.html', post=posts[post_id])

```

posts.html

```html
{% extends "layout.html" %}

{% block content %}
<h1>Posts</h1>
{% for post in posts %}
<article class="message is-primary">
    <div class="message-header">
        <a href={{url_for('posts', id=post.id)}}>{{post.title}}</a>

        <p>By: {{post.user}}</p>
    </div>
    <div class="message-body">
        {{post.text}}
    </div>
    <a>r/{{post.sub}}</a>
</article>
{% endfor %}
{% endblock %}

```

post.html

```html
{% extends "layout.html" %}

{% block content %}
<h1>Post</h1>
<article class="message is-primary">
    <div class="message-header">
        <a href={{url_for('posts', id=post.id)}}>{{post.title}}</a>

        <p>By: {{post.user}}</p>
    </div>
    <div class="message-body">
        {{post.text}}
    </div>
    <a>r/{{post.sub}}</a>
</article>
{% endblock %}
```

</details>


----------
resource
----------
- password https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/password

- flask-auth: https://git.generalassemb.ly/sf-wdi-51/flask-auth
  > pip3 install flask flask-login flask-bcrypt peewee flask-wtf
  > pip3 freeze > requirements.txt

- Step-by-step:
1) create template folder for landing.html template!
- add logo

<img src="../static/neighlogo.png" alt="neighborAlet-logo"  width="100" height="100" >

- add register html, macro for login using: 
  https://github.com/heggy231/flask-auth-login-logout
- create model to save user login info
- to check if register working: create urlfor link register (register html template, routing for register in app.py)
    created class for register form in forms.py

2) get the signin form to look like the register.html by updating class in forms.py, import macros.html

3) create database  for register, model > after that register.html so the register can insert user in `app.py` route
  - remember to call models.initialize() in app.py at this point!!


  - important resource: data type for peewee
  http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table

  - Why use peewee: It makes object out of relational table such as sql so that I do'nt have to write sql query which is hard. http://docs.peewee-orm.com/en/latest/index.html
  Peewee is a simple and small ORM. It has few (but expressive) concepts, making it easy to learn and intuitive to use.
    - a small, expressive ORM
    python 2.7+ and 3.4+ (developed with 3.6)
    supports sqlite, mysql and postgresql
    tons of extensions
- lastly check on sqllight db to see if user is created and saved in db [x]
4) Login: 
[ ] create route for login in app.py
[ ] check if data submitted during register will let user login

_________________POST FORM ___________________________
[X] 1. WTForms to create forms.py class for Post(), forms.py defines a class to represent our form. We add the fields we need which will eventually be used with a form builder on the frontend, a fairly common feature of frameworks like Flask, Django, Ruby on Rails, etc.

```
  # import the tools and fields we need
  from flask_wtf import FlaskForm as Form
  from wtforms import TextField, TextAreaField, SubmitField

  # import the Sub model
  from models import Sub

  # create the class and variables to house Field definitions
  class SubForm(Form):
    name = TextField("Name this sub")
    description = TextAreaField("Add a description for the sub here")
    submit = SubmitField('Create Sub')
```

[ ] 2. FORM now exists but we can't use it until we add it to a template!
- Create post.html template
- Use the form builder to render the form {{form.somehthing()}} - it is ok! we will find out soon! (https://git.generalassemb.ly/sf-wdi-51/Flask-Models)
```
 {% extends "layout.html" %}

  {% block content %}
    <form method="POST" action="" novalidate> // When present <form novalidate>, it specifies that the form-data (input) should not be validated when submitted
      {{ form.hidden_tag() }}

      <div>
        {{ form.name.label }}
        {{ form.name() }}
      </div>
      <div>
        {{ form.description.label }}
        {{ form.description() }}
      </div>

      {{ form.submit() }}
    </form>
  {% endblock %}
```

- [x] once user signed-in  > sees the post diary option right away in signin.html 
- [x] delete post

- [x] research chart.js, https://pythonspot.com/flask-and-great-looking-charts-using-chart-js/

- [ ] make each post in posts page a link!

- [x] share on twitter 
      https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/overview
      - 
        How to add a Tweet button to your website

        1. Create a new anchor element with a twitter-share-button class to allow the Twitter for Websites JavaScript to discover the element and enhance the link into a Tweet button. Set a href attribute value of https://twitter.com/intent/tweet to create a link to the Twitter web intent composer.

```
<a class="twitter-share-button" href="https://twitter.com/intent/tweet">
Tweet</a>
```
        2. Pre-populate Tweet text and suggest related accounts by customizing Tweet web intent query parameters.

          
        <a class="twitter-share-button"
          href="https://twitter.com/intent/tweet?text=Hello%20world">
        Tweet</a>

[ ] TODO BONUS: Future fix - need to track when user edit the post later- how does that alter the graph? endtimestamp alters