from flask import Flask
import config


__version__ = "0.0.0"


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

    load_blueprints(app)

    return app
