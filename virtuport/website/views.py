from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/signup')
def signup():
    return render_template("signup.html")