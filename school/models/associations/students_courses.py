from school import db

metadata = db.metadata

student_course = db.Table(
    "student_course",
    metadata,
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True),
)
