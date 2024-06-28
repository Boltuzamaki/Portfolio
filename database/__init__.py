from flask import Flask
from database.db import db


def create_app(database_uri, track_modifications, secret_key):
    app = Flask(__name__, static_folder="../assets", template_folder="../templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = track_modifications
    app.config["SECRET_KEY"] = secret_key

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
