from school import db

metadata = db.metadata

students_groupes = db.Table(
    "students_groupes",
    metadata,
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True),
)
