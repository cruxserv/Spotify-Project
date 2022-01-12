from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Basic database setup
db = SQLAlchemy()
DB_Name = 'database.db'

# Flask Web App setup


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    db.init_app(app)

# Blueprint setup
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

# Connect database requirements
    from .models import User

    create_database(app)

# Login app settings
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Creates database if none exists


def create_database(app):
    if not path.exists('website/' + DB_Name):
        db.create_all(app=app)
        print("Created Database!")
