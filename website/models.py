# create db schema

from enum import unique
from . import db  #from website import db (equivalent)
# in __init__.py db is defined  (db = SQLAlchemy())
# . is a package and we can access anything from __init__.py
from flask_login import UserMixin
from sqlalchemy.sql import func  # gets currentdate and time


class User(UserMixin, db.Model):
  # layout of user table
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  name = db.Column(db.String(150))
  todo = db.relationship('ToDo')  # todo list associated with user
  # FYI: db.relationship('ToDo') is a class that returns a list of ToDo objects


class ToDo(db.Model):
  # layout for ToDos
  id = db.Column(db.Integer, primary_key=True)
  todo = db.Column(db.String(100000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  # FYI: func.now() returns current date and time
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  # FYI: user.id is in small letters (user ---> User table)
  # cat_id = db.Column(db.Integer, db.ForeignKey('category.id'))


# class Category(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Colum(db.String(150))
#   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
