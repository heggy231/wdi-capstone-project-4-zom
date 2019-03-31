import datetime
from peewee import *

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('zom.db')

class User(UserMixin, Model):
  email = CharField(unique=True)
  password = CharField(max_length=100)
  joined_at = DateTimeField(default=datetime.datetime.now())

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
  content = TextField()

  class Meta:
      database = DATABASE
      order_by = ('-timestamp',)
        
        
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Post], safe=True)
  DATABASE.close()