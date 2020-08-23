from flask import Flask
import config
from peewee import *
from playhouse.flask_utils import FlaskDB


__version__ = "0.1.0"
db = FlaskDB()


def load_blueprints(app):
    if app.config["REGISTER_CORE"]:
        from flask_skeleton.core import routes

        app.register_blueprint(routes.blueprint)


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    if app.config["ENV"] == "development":
        app.config.from_object(config.DevConfig)
    elif app.config["ENV"] == "production":
        app.config.from_object(config.ProdConfig)
    db.init_app(app)

    load_blueprints(app)

    return app
