from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from school import db
from school.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('about_view.dashboard_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('about_view.dashboard_page'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('about_view.dashboard_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('role')

        if role not in ['student', 'teacher', 'director']:
            flash('Invalid role selected.', 'danger')
            return redirect(url_for('auth.register'))

        if password1 != password2:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('auth.register'))

        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password1)

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash('Account created! You are now logged in.', 'success')
        return redirect(url_for('about_view.dashboard_page'))

    return render_template('register.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home_view.home_page'))