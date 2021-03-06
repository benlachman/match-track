import os

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__,  instance_relative_config=True)

app.url_map.strict_slashes = False

env = os.environ.get('ENV', None)


if env == "prod":
    print("Loading production config")
    app.config.from_object('config.ProductionConfig')
elif env == "test":
    print("Loading testing config")
    app.config.from_object('config.TestingConfig')
else:  # dev
    print("Loading development config")
    app.config.from_object('config.DevelopmentConfig')


try:
    app.config.from_pyfile('config.py')
except FileNotFoundError as err:
    print("No instance config file found")

db = MongoEngine(app)

from . import routes
