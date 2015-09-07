from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # extension init
    db.init_app(app)

    # blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app