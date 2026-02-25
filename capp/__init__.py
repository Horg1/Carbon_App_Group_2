from flask import Flask

application = Flask(__name__, static_folder='../static')

from capp.carbon_app.routes import carbon_app
from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)
