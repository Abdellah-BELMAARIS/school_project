from flask import Blueprint, render_template
from flask_login import login_required, current_user
from school.models import StudentDB, TeacherDB, CourseDB, PrimaryClassDB

bp_about = Blueprint("about_view", __name__, url_prefix="/about")


@bp_about.route("/about")
def about_page():
    return render_template("about.html")


@bp_about.route("/dashboard")
@login_required
def dashboard_page():
    data = {}
    if current_user.role == "student":
        student = StudentDB.query.filter_by(email=current_user.email).first()
        if student:
            data["student"] = student
            data["courses"] = student.class_courses
            data["grade"] = (
                student.school_class.grade if student.school_class else "Not assigned"
            )
        else:
            data["student"] = None
    elif current_user.role == "teacher":
        teacher = TeacherDB.query.filter_by(email=current_user.email).first()
        if teacher:
            data["teacher"] = teacher
            data["courses"] = teacher.class_courses
            data["groups"] = teacher.groups
            data["grade"] = (
                teacher.school_class.grade if teacher.school_class else "Not assigned"
            )
        else:
            data["teacher"] = None
    elif current_user.role == "director":
        data["total_students"] = StudentDB.query.count()
        data["total_teachers"] = TeacherDB.query.count()
        data["total_courses"] = CourseDB.query.count()
        data["total_classes"] = PrimaryClassDB.query.count()
    return render_template("dashboard.html", **data)
