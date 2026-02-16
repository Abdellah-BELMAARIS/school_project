from school import db

meta = db.MetaData()

students_course = db.Table(
    "students_course",
    meta,
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True),
)
