from flask import Flask, render_template, Request, url_for, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
import os


views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    songs = os.listdir("website/static/assets/")
    return render_template("home.html", user=current_user, songs=songs)
