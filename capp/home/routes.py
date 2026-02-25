from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/')
@home.route('/home')
def home_home():
    return render_template('home.html', title='home')


@home.route('/create-chat')
def create_chat():
    return render_template('create_chat.html', title='Create Chat')


@home.route('/view-chats')
def view_chats():
    return render_template('view_chats.html', title='View Chats')


@home.route('/statistics')
def statistics():
    return render_template('statistics.html', title='Statistics')


@home.route('/students-apps')
def students_apps():
    return render_template('students_apps.html', title='Students Apps')


@home.route('/haugesund')
def haugesund():
    return render_template('haugesund.html', title='Haugesund')


@home.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')
