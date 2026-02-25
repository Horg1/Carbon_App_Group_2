from flask import Blueprint, render_template

carbon_app = Blueprint('carbon_app', __name__)


@carbon_app.route('/carbon-app')
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')


@carbon_app.route('/carbon-app/new-entry')
def new_entry():
    return render_template('carbon_app/new_entry.html', title='new_entry')


@carbon_app.route('/carbon-app/your-data')
def your_data():
    return render_template('carbon_app/your_data.html', title='your_data')
