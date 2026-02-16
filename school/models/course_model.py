from datetime import datetime, timezone
from school import db


class CourseDB(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)



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

    students = db.relationship(
        "StudentDB", secondary="students_courses", back_populates="class_courses"
    )
    teachers = db.relationship(
        "TeacherDB", secondary="teachers_courses", back_populates="class_courses"
    )
    classes = db.relationship(
        "SchoolClassDB", secondary="school_class_courses", back_populates="class_courses"
    )
    groups = db.relationship(
        "GroupDB", secondary="groups_courses", back_populates="courses"
    )
    