from os import name
from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
# FYI: inverse cannot be obtained. if i give pw, it will always generate the same hash
# but if we have hash we cannot get the pw ever again
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('loginEmail')
    password = request.form.get('loginPassword')
    user = User.query.filter_by(email=email).first()
    if user:
      print("User present !!!")
      if check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        # FYI: remember=True means that the user will be logged in even if the page is reloaded
        return redirect(url_for('views.home'))
      else:
        print("Incorrect")
        flash('Incorrect password, try again.', category='danger')
    else:
      flash('Email does not exist.', category='danger')

  return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
# FYI: @login_required is a decorator that checks if the user is logged in or not
def logout():
  logout_user()
  return redirect(url_for('auth.login'))
  # return render_template('logout.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    registerName = request.form.get('registerName')
    registerEmail = request.form.get('registerEmail')
    registerPassword = request.form.get('registerPassword')
    registerConfirmPassword = request.form.get('registerConfirmPassword')

    user = User.query.filter_by(email=registerEmail).first()
    if user:
      flash('Email aleady exists.', category='danger')
    elif len(registerEmail) < 4:
      flash('Email must be greater than 3 characters', category='danger')
    elif len(registerName) < 2:
      flash('Name must be greater than 1 character', category='danger')
    elif registerPassword != registerConfirmPassword:
      flash('Passwords do not match', category='danger')
    elif len(registerPassword) < 6:
      flash('Password must be at least 6 characters', category='danger')
    else:
      new_user = User(name=registerName,
                      email=registerEmail,
                      password=generate_password_hash(registerPassword,
                                                      method='pbkdf2:sha256'))
      db.session.add(new_user)
      db.session.commit()
      # add user to db
      login_user(new_user, remember=True)

      flash('Account created!', category='success')
      return redirect(url_for('views.home'))
    # data = request.form
    # print(data)
  return render_template('register.html', user=current_user)
