from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
  # render temp - templates/index.html
  return render_template("home.html")
