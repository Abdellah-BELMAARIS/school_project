from school import db

metadata = db.metadata

teachers_courses = db.Table(
    "teachers_courses",
    metadata,
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True),
)
