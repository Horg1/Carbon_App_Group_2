from flask import Blueprint, flash, redirect, render_template, url_for

from capp.users.forms import LoginForm, RegistrationForm

users = Blueprint('users', __name__)


REGISTERED_USERS = {}


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        REGISTERED_USERS[form.email.data] = {
            'username': form.username.data,
            'password': form.password.data,
        }
        flash(f"Account created for {form.username.data}. You can now sign in.", 'success')
        return redirect(url_for('users.login'))

    return render_template('users/register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = REGISTERED_USERS.get(form.email.data)

        if user and user['password'] == form.password.data:
            flash('Login successful. You can start to use the app.', 'success')
            return redirect(url_for('home.home_home'))

        flash('Login failed. Please check your credentials and try again.', 'danger')
        return redirect(url_for('users.login'))

    return render_template('users/login.html', title='Login', form=form)
