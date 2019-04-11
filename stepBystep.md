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

- heggy initial run command
#Flask command Models RUN FLASK

- ********** how to run flask start flask https://git.generalassemb.ly/sf-wdi-51/Flask-Templates/blob/master/README.md https://git.generalassemb.ly/sf-wdi-51/intro_to_flask
>$ mkdir flask-intro && cd flask-intro
>$ pip3 install virtualenv
>$ virtualenv .env -p python3
>$ source .env/bin/activate
> pip3 install -r requirements.txt
> python3 app.py

>$ pip3 install flask flask-login flask-bcrypt peewee flask-wtf flask-cors
>$ pip3 freeze > requirements.txt
> python3 app.py
if I got this app from online (https://git.generalassemb.ly/sf-wdi-51/intro_to_flask#dependencies)

> python3 app.py // run th app
I expect to see it running `http://localhost:8000/`

second time
>$ virtualenv .env -p python3
>$ source .env/bin/activate
> pip3 install -r requirements.txt
> python3 app.py // run th app
I expect to see it running `http://localhost:8000/`


>$ pip3 install virtualenv
>$ virtualenv .env -p python3
>$ source .env/bin/activate
> pip3 install -r requirements.txt
> python3 app.py // run th app


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
[x] create route for login in app.py
[x] check if data submitted during register will let user login

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

[x] 2. FORM now exists but we can't use it until we add it to a template!
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

* Create new post is happening inside `signin.html`
```
  {% if current_user.is_authenticated %}
    <form method="POST" action="{{url_for('post')}}" class="form">
      {{ postform.hidden_tag() }}
      {% for field in postform %} // this is a macro
        {{ render_field(field) }}
      {% endfor %}
      <button class="btn btn-dark" type="submit" id="submit">Post Diary</button>
    </form>
  {% endif %}
```
  based on this Post model fields are created inside of signin.html
```
  class Post(Model):
    starttimestamp = DateTimeField()
    endtimestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(
      model=User,
      backref='posts'
    )
    title = CharField()
    content = TextField()
```

- [x] delete post

- [x] research chart.js, https://pythonspot.com/flask-and-great-looking-charts-using-chart-js/
  https://www.chartjs.org/docs/latest/getting-started/installation.html
  - look for cdn Chart.min.js file
  https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js
  - https://www.patricksoftwareblog.com/creating-charts-with-chart-js-in-a-flask-application/
  - creating chartjs https://www.chartjs.org/docs/latest/getting-started/usage.html#creating-a-chart
  - really good resource for chart js
    https://www.sitepoint.com/fancy-responsive-charts-with-chart-js/
  1) add script tag inside of layout.html inside of head tag
      <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js"></script>

      https://codepen.io/chartjs/pen/bWeqxB
      Chart.js look (make it blue)
      - blue dataset backgroundcolor hex: "rgba(10,22,195,0.2)" https://www.color-hex.com/color/0a16c3
      - darker blue dataset border color https://www.color-hex.com/color/438e94

    https://codepen.io/heggy231/pen/jRVzzE
  datasets: [{
    label: "Dataset #1",
    backgroundColor: "rgba(10,22,195,0.2)",
    borderColor: "rgba(67,142,148,1)",
    borderWidth: 2,
    hoverBackgroundColor: "rgba(255,99,132,0.4)",
    hoverBorderColor: "rgba(255,99,132,1)",
    data: [65, 59, 20, 81, 56, 55, 40],
  }]

fillColor: is background graph color
strokeColor: is outline color


https://pythonspot.com/flask-and-great-looking-charts-using-chart-js/
label: [

]
2) year.total_seconds() convert year to seconds()  https://docs.python.org/3/library/datetime.html
http://strftime.org/
label Mon %a 	Weekday as locale’s abbreviated name. 	Mon

3) rounding
  jinja rounding: Note that even if rounded to 0 precision, a float is returned. If you need a real integer, pipe it through int:

  {{ 
    42.55|round|int 
  }}

  {{ 
    ((post.endtimestamp - post.starttimestamp).total_seconds() / 60) | round | int 
  }}
- [x] share on twitter 
      https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/overview

## How to add a Tweet button to your website

        1. Create a new anchor element with a twitter-share-button class to allow the Twitter for Websites JavaScript to discover the element and enhance the link into a Tweet button. Set a href attribute value of https://twitter.com/intent/tweet to create a link to the Twitter web intent composer.

```
<a class="twitter-share-button" href="https://twitter.com/intent/tweet">
Tweet</a>
```
        2. Pre-populate Tweet text and suggest related accounts by customizing Tweet web intent query parameters.

          
        <a class="twitter-share-button"
          href="https://twitter.com/intent/tweet?text=Hello%20world">
        Tweet</a>


[x] bug on user time signed in issue: Usermix doesn't yet have login info to get the timestamp
![userMix](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-06%20at%208.21.03%20PM.png?1554611746673)
```
  myuser = models.User.get(models.User.id == g.user.userid)
  myuser.login_time = login_time 
  myuser.save() # this is errors out due to UserMIXIN has not yet set the user info
```
    resolved: Flask Cookies: https://www.tutorialspoint.com/flask/flask_cookies.htm

      # remember to import make_response, request from flask for cookie!
        resp = make_response(render_template('signin.html', form=form, current_user=current_user, postform=postform)) # https://stackoverflow.com/questions/46661083/how-to-set-cookie-in-python-flask, http://flask.pocoo.org/docs/1.0/api/#flask.Response.set_cookie
        resp.set_cookie('login_time', login_time.strftime('%Y-%m-%d  %I:%M%p') )
        
[ ] TODO BONUS: Future fix - need to track when user edit the post later- how does that alter the graph? endtimestamp alters

[x] bug fix: https://stackoverflow.com/questions/27606653/oserror-errno-8-exec-format-error   #!/usr/bin/env python
add that top of app.py for it to find the erron error, this specifies that my files are python so compile it with python engine

- [ ] CREATE profile page which will have the graphs and list all posts in posts page a link!

- When designing
 
  * input field fake vertical-align top to work with padding trick:
  https://codepen.io/heggy231/pen/xeEPJW?editors=1100
*** forms.py) ****
class PostForm(Form): #pass in Form class obj to inherit StringField() method and TextField

  title = StringField(  << title is class, id
    'Title',  <<< this is placeholder
    validators=[
      DataRequired()
    ])
  content = TextField(
    'Tell your story...',  
    validators=[
      DataRequired()
    ])
- Delete
  1) create url for the function delete
  <a href={{url_for('delete_post', postid=post.id)}}><i class="fas fa-trash-alt"></i></a>

  2) create delete_post route in app.py
  @app.route('/post/<postid>/delete')
@login_required # todo: before submitting activate this to prevent users to delete w/o login
def delete_post(postid):
    post_id = int(postid)
    post = models.Post.get(models.Post.id == post_id)
    post.delete_instance()
    return redirect(url_for('posts'))

* Note: models.Post.id is every model has an id it's ok if you don't see the id inside of models.Post 

class Post(Model):
  starttimestamp = DateTimeField()
  endtimestamp = DateTimeField(default=datetime.datetime.now)
  user = ForeignKeyField(
    model=User,
    backref='posts'
  )
  title = CharField()
  content = TextField()

  class Meta:
      database = DATABASE
      order_by = ('-endtimestamp',) #latest one comes on top


- note: return redirect(url_for('posts'))  // creating url for posts function in my app.py
  https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for/35936261#35936261

  @app.route('/questions/<int:question_id>'):    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
  def find_question(question_id):  
      return ('you asked for question{0}'.format(question_id))

    For the above we can use: 'find_question' is function name that I define inside app.py, question.id is automatically assigned for every instance of class.
    <a href = {{ url_for('find_question' ,question_id=question.id) }}>Question 1</a>



[ ] editing post:
  1) click pencil icon and call posts route pass <id> else stmt >
    else:
      post_id = int(id)
      # .get() get us the Post.id = post's id that user selected
      post = models.Post.get(models.Post.id == post_id)
      # then show `post.html` info
      return render_template('post.html', post=post)

   
    <a href={{url_for('posts', id=post.id)}}>{{post.title}} <i class="fas fa-pencil-alt"></i></a>

  2) once inside of http://localhost:8000/posts/2
  it is rendering post.html with user selected id (models.Post.get(models.Post.id == post_id))


[ ] Bug when user press enter (from laptop) well user wouldn't really press enter in phone would they?  it submits in the middle of posting very annoy thing how to prevent that from happening?
  () try prevent default form e.prevent default form behavior?

[ ] create seed data based on these diary entries
  - Title: Friend (Obvious Child)
    Content: I guess diary suppose to be honest.  Let me tell you little bit about me. As they say, I like my man like how I like my coffee.  disgusting?  like very weak and bitter uuuhhhhmmmm... Cold, not sweet at all ....  very gritty on the bottom as well?  if you know coffee like that.  Just like, what is your Number?  Now that we are all picturing a very filthy bottom.  I think it's time to introduce to one!!  And she is my best friend in the entire world.  I think you will love her just as much as I do.

  - Title: Box (Obvious Child)
    Content: Wow, wow.  I did the first scream for screaming and then the second scream from scaring myself from the first scream.  Yeah, I saw that.  I'm gonna come in now, ok? Yeah tada.  What are you doing here?  You said you worked here so.  Oh sure,  Oh! savage detectives.  This book's amazing.  Well, it can be yours for 99 cents.  Hey I just passed by a Mexican food truck on the way over here.  Do you wanna get a bite?  oooo ahhhh I.. When we hung out before you said, ahhh..  You said that you could Mouth f* the S* out of the burritos.  Oh G* D* I*.  Ok, Yeah?  Also, do you remember urinating in the street?  hmm among other things.  What?

  - Money
    I can't afford this.  It is almost all of my rent money.  Is there a discount?  No this has a great care plan.  Do you have any friends and family who can rent you some cash?  mmm 

  - Child
    I am not ready to have my own kids.  How can I have kids when I can't turn off the TV.  Nobody knows how to do their taxes.  No I am not going to work for your students. 

  - Crocs
    Oh you have problem with my shoes?  These are my moms.  Do you want to try them on?  Pst, No.  Alright, yeah.  That's amazing.  I don't do hard drugs.  But I imagine this would be like shooting he*.  Yeah they are so soft they are made out of angels ti* skins.  Well, and she said that.

- Deploy to Heroku : http://docs.peewee-orm.com/en/latest/peewee/database.html, 
  - sql_lite is not for production db therefore we need to convert it to postgres which will save the db each time heroku runs my app
  step1) http://docs.peewee-orm.com/en/latest/peewee/database.html#database


https://git.generalassemb.ly/SF-WDI/flask-deployment
https://git.generalassemb.ly/sf-wdi-51/project-03
https://nbor-alert-heroku.herokuapp.com/
http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud/page/5

# initialise a database
# db = PostgresqlDatabase(
#     'database_name',  # Required by Peewee.
#     user='postgres',  # Will be passed directly to psycopg2.
#     password='secret',  # Ditto.
#     host='db.mysite.com')  # Ditto.

### create a nav bar:
  - https://www.skillshare.com/lists/Coolors/102?coupon=coolors2m&irgwc=1&clickid=wpB22B3x6xGgVqr00IxYZyqoUkmSo5QvuVn1Q00&utm_content=4650&utm_term=Online%20Tracking%20Link&utm_campaign=coolors_&affiliateRef=125995&utm_medium=affiliate-referral&utm_source=IR

#### dark theme:
https://codepen.io/HarlemSquirrel/pen/NdMebZ/
- gradually change the color background turn on the light
https://codepen.io/amitsheen/pen/bMBgZm
https://us.sirthelabel.com/

- dark theme scroll bar
https://codepen.io/subfauna/pen/CLtmF

- yellow and dark blue background
https://codepen.io/tomhodgins/pen/OMgPOY

- color research
https://www.sleep.org/articles/best-colors-for-sleep/
based on sleep.org (National Sleep Foundation )

- sleepy https://i.pinimg.com/originals/12/03/d8/1203d8dbd23787123dc714de1c07df09.gif
- sleepy cat https://img.buzzfeed.com/buzzfeed-static/static/2014-04/campaign_images/webdr06/22/9/soothing-gifs-to-help-you-unwind-2-1000-1398172942-25_dblbig.jpg
- fire beache https://images.hellogiggles.com/uploads/2016/06/20061732/beachhh2.gif

- add twitter card when user saves it on their phone

- diary as a card with animation

- accessible
  * Canvas element with accessible name and role via ARIA:
  http://pauljadam.com/demos/canvas.html

- sheep transparent background
http://www.pngmart.com/image/tag/sheep
  mom baby sheep http://www.pngmart.com/image/126858

  - video: https://youtu.be/jSU18TounoI


- color for blue
https://www.colorhexa.com/f0f8ff


- tap target: mobile first design tap buttons links: 10 millimeters wide or half an inch - works out about 40 css px.
  * fat fingers, fat thumbs: at least give 48px x 48px
  Tap targets should be bigger than the average finger.  To ensure all of your elements are at least that size, add `min-height: 48px;`
  `min-width: 48px;` to every tappable element.

  `height`, `width` alone can be dangerous b/c it won't allow the element to resize if the content inside of it is bigger than the container.

```
nav a, button {
  min-height: 48px;
  min-width: 48px;
}
```


- pokemon lorem ipsum
http://pokemipsum.com/

Title: Sting Kadabra Zweilous
Content: Grass Splash Celebi the enemy Pokemon fainted Maractus Hitmonchan Seismitoad. Vermilion City Houndour Aipom Cresselia Seaking Entei Lugia. Slash Metang Grovyle Super Potion Musharna Beheeyem Marowak. Charmander Bagon Munna Drifloon Sigilyph Gloom I'm on the road to Viridian City. Ruby Genesect Vaporeon Team Rocket Munchlax Eelektross Sand-Attack. 

- dark moon water giphy
https://giphy.com/gifs/water-moon-full-zxpLFGndoTuHS

starDarkCelticSky img for title
https://collhotel.com/coll-dark-sky/
https://www.google.com/search?q=dark+sky&rlz=1C5CHFA_enUS714US716&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjJmfiit8fhAhW6HTQIHZ5LBb0Q_AUIDigB&biw=951&bih=596#imgdii=lfoOMUN1MUXo-M:&imgrc=iaFfsg9hFj7OTM:

- dark moon ocean
https://giphy.com/gifs/water-moon-full-zxpLFGndoTuHS/links

- owl shake cool head giph
https://giphy.com/allyouneediswall

- golden sky
https://aaronchang.com/product/slate/

- flask deployment:
my heroku deployed site: https://zom-flask.herokuapp.com/
  * https://git.generalassemb.ly/SF-WDI/flask-deployment
  skip step 9)
  ```
  from playhouse.db_url import connect
  DATABASE = connect(os.environ.get('DATABASE_URL'))
  ```
  skip step 11)
  skip step 12) // basically anything related to Postgres


- how to comment out things in Jinja
{# #} // as if you are commenting python and inserting python variable inside of Jinja