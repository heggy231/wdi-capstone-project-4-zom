# <img src="https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FZom.png?1553973356562" height="60"> Project 4 - Final Project

## <a href="https://zom-heroku.herokuapp.com/" target="_blank">**DEMO**</a>

### Motivation to build this project?
Have you experienced not being able to fall into sleep?  Do you remember why?
<a href="https://www.prevention.com/health/sleep-energy/a20437995/10-reasons-you-cant-sleep/" target="_blank">**Top 1**</a> reason why most people can't sleep is that they think too much in bed.  
<img src="https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-11%20at%2010.06.47%20PM.png?1555045637025">

I suffered from **insomnia** where I couldn't sleep for 2 straight weeks.  While looking all over to find how to fall asleep, I ran into <a href="https://www.goodreads.com/book/show/16087720-goodnight-mind" target="_blank">Goodnight mind</a> book by Dr. Carney who is one of Canada's leading experts in psychological treatments for insomnia.  Following that book cured me of insomnia.  Today, I am presenting you with one of most effective technique that I learned that helped me go to sleep.

- Goal: Zom app is a private space for sleepless to brain dump all of their worries and quiet down their mind.

<img src="https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-11%20at%2010.01.54%20PM.png?1555045401078" width="50%" height="50%">



==================================

### Technology Python Flask Peewee SQL Stack

* Flask: Flask as the core framework for Python.
* Peewee: object-relational mapper (ORM) implementation for bridging relational data and Python objects.

* Jinja: designer-friendly templating language for Python
* SQLite: Lib that implements small, fast, self-contained, high-reliability, full-featured, SQL database engine

##### Other Technologies Used

* JWT | bcrypt - Authentication
    * A JSON web token, encrypted container format that is used to securely transfer information between two parties. JWTs are credentials, which can grant access to resources.
* Cookies - Registering login time
* Twitter API - Share my diary

===================================

### Process/ Approach

* Research

* User Story
    * User can visit / to see a landing page (signin.html).
    * User can Login or Register.
    * Logged in User can post diary from landing page 
    (signin.html).
    * Logged in User can navigate to user's profile (posts.html).
    * Logged in User can create/edit/update/delete User's diary entries from User's profile page (posts.html).
    * Logged in User can see User's list of diary posts on profile page (posts.html)
    * Logged in User with a post can view User's post (posts/id.html)
    * Logged in User can logout and be redirected to signin page.

* Wireframes

![Wireframes Mobile](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FwireframeMobile.png?1555075487729)

![Wireframes Desktop](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FwireframeDesk.png?1555075489743)

* ERD (Entity Relationship Diagram)

![ERD](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FERD.png?1555075345890)

* System Architecture
![system architecture](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FsystemArchitecture.png?1555912144408)

* Sprint 1: Back-End Build Out
    * Define Peewee, WTForms
    * Define login, DB
    * Create Models
    * JWT, bcrypt Auth
    * Sign In/Out
    * Collect user data logic
    * Visualize data

* Sprint 2: Front-End Jinja Templating
    * Create Routes, Controllers
    * Back-End Testing
    * Use Postman to test all CRUD (GET, POST, PUT, DELETE)
    * Skeleton- create forms
    * Logic/Functionality
    * Test Front-End, Back-End connection
    * Heroku

* Sprint 3: Front-End Polish, documentation
    * Mobile first styling
    * README.md
    * Presentation slides
    * Fonts/Styles/CSS
    * UI/UX, Flow etc
    * Navbar overlay, animation
    * Built out, test
    * Responsive check

===================================

## Unsolved Problems
* Notifications: Flash Error message to show up as modal.
* Help robots
* Hover effect chartJS
* Desktop UI
* Deploy with secret key hidden on heroku
* Deploy with Postgres and still working

### Code blocks...

![user login time](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-12%20at%206.36.47%20AM.png?1555076260987)

![edit](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-12%20at%206.39.21%20AM.png?1555076439504)

![edit route](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-12%20at%206.40.20%20AM.png?1555076439610)

![chartJS](https://cdn.glitch.com/cb093bfd-142f-45b3-bdb4-52ff49e0a1c2%2FScreen%20Shot%202019-04-12%20at%206.44.19%20AM.png?1555076683323)
## Challenges/Wins

#### Challenges
> Catch the login time data.  At first create a new column on User DB but Python told me user properties are not set yet.  I went for new direction of setting the cookie.  
> Focus on one thing at a time.
> jQuery not listening with Flask.
> Heroku with Postgres DB
> Learning to switch gear from Python, Jinja, Peewee

#### Wins
> Step-by-step...was able to move forward by breaking into small bite-size chunks.
> Learned how Jinja templating, how data gets passed between routes.  I got real good at redirect, URL_For.
> Try it even though I am not sure if it will work and build as I get yelled by Python.
> Build locally, from the ground up, not from a tutorial!


#### THANK YOU
To everyone, especially the instructors- Isha, Dalton, Brock!