from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
alembic = Alembic()
login_manager = LoginManager()

DB_NAME = "school.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["ALEMBIC_CONTEXT"] = {"render_as_batch": True}

    db.init_app(app)
    alembic.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."

    from .views import bp_home, bp_about
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_about)

    from ..auth import auth
    app.register_blueprint(auth)

    from .models import (
        StudentDB, ParentDB, TeacherDB, CourseDB, GroupDB,
        PrimaryClassDB, CollegeClassDB, HighSchoolClassDB,
        groups_course, groups_teacher, school_class_course,
        students_course, students_groupes, teachers_course,
        User
    )

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

def create_database(app):
    if not path.exists("school/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")
