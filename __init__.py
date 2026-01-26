from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

DB_NAME = "school.db"


def create_app(test_config=None):
    from db_init import init_app

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="devpulse",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, DB_NAME)}",
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path, exist_ok=True)

    except OSError:
        pass

    init_app(app)

    from .models import student, teacher, courses


    app.register_blueprint(student.bp)
    app.register_blueprint(courses.bp)
    app.register_blueprint(teacher.bp)

    cretate_database(app)

    return app


def cretate_database(app):
    db_path = os.path.join(app.instance_path, DB_NAME)
    if not os.path.exists(db_path):
        with app.app_context():
            from .db_init import init_db

            init_db()
            print("Database created")
