import datetime
from peewee import * # peewee is a small and simple ORM, like mongoose but simpler

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('zom.db') # We use the built in SqliteDatabase() function from peewee to save a reference to a DB file to a DATABASE variable

class User(UserMixin, Model): # User model with email, pwd, joinDate!
  email = CharField(unique=True)
  password = CharField(max_length=100)
  joined_at = DateTimeField(default=datetime.datetime.now())
  signedin_at = DateTimeField(default=datetime.datetime.now(), null=True) # when user logs in this gets updated

  class Meta:
    database = DATABASE
    order_by = ('-joined_at',)

  def get_posts(self):
    return Post.select().where(Post.user == self)

  @classmethod
  def create_user(cls, email, password):
    try:
      cls.create(
          email=email,
          password=generate_password_hash(password)
      )
    except IntegrityError:
        raise ValueError("User already exists")

class Post(Model):
  timestamp = DateTimeField(default=datetime.datetime.now)
  user = ForeignKeyField(
    model=User,
    backref='posts'
  )
  title = CharField()
  content = TextField()

  class Meta:
      database = DATABASE
      order_by = ('-timestamp',)
        
  class Time(Model):
    user_id= IntegerField()
    post_id= IntegerField()
    class Meta:
        database = DATABASE
        
def initialize(): # Initialize a connection to the DATABASE, create a table for the User, Post models; then close the connection
  DATABASE.connect()
  DATABASE.create_tables([User, Post], safe=True)
  DATABASE.close()