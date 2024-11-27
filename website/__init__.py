from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'qwertyuiop'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .views import views
  from .auth import auth
  # prefix/anything_in_auth_or_views
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  from .models import User, ToDo
  create_database(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  return app


# FYI: check if db exists or not. If it exist use it, else create it
def create_database(app):
  if not path.exists('instance/' + DB_NAME):
    with app.app_context():
      db.create_all()
    print('Created Database!!')
  else:
    print("Already DB Exists")
