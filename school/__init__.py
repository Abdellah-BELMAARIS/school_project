from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask import Flask
from os import path

db: SQLAlchemy = SQLAlchemy()
DB_NAME: str = "school.db"
alembic: Alembic = Alembic()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import bp_home, bp_about

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_about)

    from .models import StudentDB, ParentDB, TeacherDB, CourseDB, GroupDB, PrimaryClassDB, CollegeClassDB, HighSchoolClassDB

    with app.app_context():
        db.create_all()


    return app


def create_database(app):
    if not path.exists("school/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")

