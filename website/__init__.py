from flask import Flask, render_template


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'qwertyuiop'

  from .views import views
  from .auth import auth
  # prefix/anything_in_auth_or_views
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  return app
