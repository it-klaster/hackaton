from flask import Flask

from python_apps.api.database import db
from python_apps.api.models import *
from python_apps.api.settings import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

