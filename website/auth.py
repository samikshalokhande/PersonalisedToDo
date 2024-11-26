from flask import Blueprint
from flask import Flask, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
  return render_template('login.html')


@auth.route('/logout')
def logout():
  return render_template('logout.html')


@auth.route('/register')
def register():
  return render_template('register.html')