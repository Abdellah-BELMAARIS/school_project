from datetime import datetime, timezone
from school import db


class SchoolClassDB(db.Model):
    __tablename__ = "school_classes"

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(100), nullable=False)

    type = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "school", "polymorphic_on": type}

    created_at = db.Column(
        db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    students = db.relationship("StudentDB", back_populates="school_class")
    groups = db.relationship("GroupDB", back_populates="school_class")
    teachers = db.relationship("TeacherDB", back_populates="school_class")
    courses = db.relationship(
        "CourseDB", secondary="school_class_course", back_populates="school_classes"
    )


class PrimaryClassDB(SchoolClassDB):
    __tablename__ = "primary_classes"

    id = db.Column(db.Integer, db.ForeignKey("school_classes.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "primary",
    }


class CollegeClassDB(SchoolClassDB):
    __tablename__ = "college_classes"

    id = db.Column(db.Integer, db.ForeignKey("school_classes.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "college",
    }


class HighSchoolClassDB(SchoolClassDB):
    __tablename__ = "high_school_classes"

    id = db.Column(db.Integer, db.ForeignKey("school_classes.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "high_school",
    }
