from flask import Flask
from flask_cors import CORS

from .model import db
from .view import home_bp
from .config import Config
from .blueprints.edit_user.view import edit_bp
from .blueprints.login.view import login_bp
from .blueprints.register.view import register_bp
from .blueprints.user_profile.view import userprofile_bp
from .blueprints.token_auth.otherServices_view import tauth_bp


def auth_service():

    app = Flask(__name__)
    CORS(app)

    # Registering all the blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(userprofile_bp)
    app.register_blueprint(tauth_bp)
    app.register_blueprint(edit_bp)

    # Load the config file from the Config object
    app.config.from_object(config.Config)

    # Instantiate the db
    db.init_app(app)

    return app
