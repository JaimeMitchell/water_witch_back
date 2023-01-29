from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        # GET THEE TO MY DATABASE
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        # used for running testing routes
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup. Why is Fountain greyed out???
    from app.models.fountain import Fountain

    # SQLAlchemy initializes with Flask and migrate/alembic initializes with flask app and database
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here and import them to my routes
    from.routes import fountain_bp
    app.register_blueprint(fountain_bp)

    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app
