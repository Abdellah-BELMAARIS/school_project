from datetime import datetime, timezone
from school import db


class GroupDB(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    school_class_id = db.Column(
        db.Integer, db.ForeignKey("school_classes.id"), nullable=False
    )
    created_at = db.Column(
        db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    school_class = db.relationship("SchoolClassDB", back_populates="groups")

    teachers = db.relationship(
        "TeacherDB", secondary="groups_teachers", back_populates="groups"
    )
    students = db.relationship(
        "StudentDB", secondary="students_groups", back_populates="groups"
    )
    courses = db.relationship(
        "CourseDB", secondary="groups_courses", back_populates="groups"
    )