import os
from flask import Flask
from .models import db
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'moto')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:akul@localhost:5432/akul')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app