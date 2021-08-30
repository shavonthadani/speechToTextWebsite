#auth.py
#Backend for login page
#Developer: Shavon Thadani
#23/08/'21
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth',__name__)
from flask_login import login_user, login_required, logout_user, current_user

#login page
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!',category = 'success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorect password, try again.', category='error')
        else:
            flash("Email does not exist.",category='error')
    return render_template("login.html", user=current_user)

#logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#sign up page
@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email =request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists",category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.',category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.',category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 6 characters.',category='error')
            pass
        else:
            new_user = User(email=email,first_name=first_name,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash('Account created.',category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user = current_user)
