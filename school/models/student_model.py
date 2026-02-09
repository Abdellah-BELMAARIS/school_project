from sqlalchemy import ForeignKey
from school import db


from datetime import datetime, timezone


class StudentDB(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    parent_id = db.Column(db.Integer, ForeignKey("parents.id"), nullable=False)
    school_class_id = db.Column(
        db.Integer, ForeignKey("school_classes.id"), nullable=False
    )
    student_id = db.Column(db.String(50), unique=True, nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    parent = db.relationship("ParentDB", back_populates="students")
    school_class = db.relationship("SchoolClassDB", back_populates="students")

    courses = db.relationship(
        "CourseDB", secondary="student_course", back_populates="students"
    )
    groups = db.relationship("GroupDB", secondary="group_student", back_populates="students")
