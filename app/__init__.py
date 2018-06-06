import os

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# database variable initialization
db = SQLAlchemy()

def create_app():
    config_env = os.getenv('APP_CONFIG_ENV')

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_env])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    return app
