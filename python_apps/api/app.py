from flask import Flask

from database import db
from models import *
from settings import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


app = create_app()
c = app.config

app.logger.info('>>>>> Starting development server at http://{}/<<<<<'.format(c['FLASK_SERVER_NAME']))

if __name__ == "__main__":
    app.run(debug=c['DEBUG'], host='0.0.0.0', port=c['PORT'])
