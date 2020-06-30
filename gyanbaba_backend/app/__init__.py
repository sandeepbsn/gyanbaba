# this will do ur create app
from flask import Flask 
from config import app_config
from flask_migrate import Migrate
from .models import *
from .routes import slash as slash_blueprint


# db=SQLAlchemy()


def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    migrate=Migrate(app,db)
    app.register_blueprint(slash_blueprint,url_prefix='/slash')


    # @app.route('/')
    # def home():
    #     return 'Welcome'

    return app