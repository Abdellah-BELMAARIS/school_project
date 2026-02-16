from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask import Flask
from os import path


db: SQLAlchemy = SQLAlchemy()
alembic: Alembic = Alembic()

DB_NAME: str = "school.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    
    # ADD THIS LINE TO ENABLE BATCH MODE FOR SQLITE:
    app.config["ALEMBIC_CONTEXT"] = {"render_as_batch": True}

    db.init_app(app)
    alembic.init_app(app)

    from .views import bp_home, bp_about

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_about)

    from .models import (
        StudentDB,
        ParentDB,
        TeacherDB,
        CourseDB,
        GroupDB,
        PrimaryClassDB,
        CollegeClassDB,
        HighSchoolClassDB,
    )
    from .models import (
        groups_course,
        groups_teacher,
        school_class_course,
        students_course,
        students_groupes,
        teachers_course,
    )

    # with app.app_context():
    #     db.create_all()

    return app


def create_database(app):
    if not path.exists("school/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")
