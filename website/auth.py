from flask import Flask, render_template, request, url_for, Blueprint, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user, login_user, current_user
from .models import User
from . import db

# Uses the blueprint module to create the app structure
auth = Blueprint('auth', __name__)

# ---------------------------------------------------------------------
# Login page has 2 basic uses, one is to GET data from 
# webserver and show it on your screen, the other is to POST
# info user puts into the form to the database to check credentials.
# -------------------------------------------------------------------

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        # Query database for username and return account for password authentication
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect credentials, try again.', category='error')
        else:
            flash(
                'Error. Username does not yet exist. Please try again, or create account.', category='error')

    return render_template("login.html", user=current_user)

# Logout system


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# -------------------------------------------------------------------------------------------
# Sign-up system gathers info from the web form, tests for parameters, then adds new account
# to database, and logs new user in
# -------------------------------------------------------------------------------------------

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        username = request.form.get('username')
        payment_method = request.form.get('payment-method')
        card = request.form.get('card')

        # Testing for correct information on form
        user = User.query.filter_by(username=username).first()
        # Query database for username and return account for password authentication
        if user:
            flash('Error. Username already exists.', category='error')
        elif len(email) < 8:
            flash('Error. Email must be greater than 3 characters.',
                  category='error')
        elif len(card) < 15:
            flash('Error. Card must be at least 15 characters', category='error')
        elif len(name) < 2:
            flash('Error. Name must be greater than 2 characters.',
                  category='error')
        elif len(password) < 8:
            flash('Error. Password must be at least 8 characters.',
                  category='error')
        else:
            # create new user in database and login user
            new_user = User(email=email, name=name, username=username, card=card,
                            payment_method=payment_method, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
