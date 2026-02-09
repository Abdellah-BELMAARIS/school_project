from school import db

metadata = db.metadata

teacher_course = db.Table(
    "teacher_course",
    metadata,
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True),
)
