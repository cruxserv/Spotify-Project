from . import db
from flask_login import UserMixin

# Basic database in project files setup


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    payment_method = db.Column(db.String(25))
    card = db.Column(db.Integer)
