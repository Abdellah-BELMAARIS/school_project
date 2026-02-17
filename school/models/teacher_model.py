from datetime import datetime, timezone
from school import db

class TeacherDB(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    school_class_id = db.Column(
        db.Integer, db.ForeignKey("school_classes.id"), nullable=False
    )
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"), nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

    course = db.relationship("CourseDB", foreign_keys=[course_id])

    school_class = db.relationship("SchoolClassDB", back_populates="teachers")
    groups = db.relationship(
        "GroupDB", secondary="groups_teacher", back_populates="teachers"
    )
    class_courses = db.relationship(
        "CourseDB", secondary="teachers_course", back_populates="teachers"
    )