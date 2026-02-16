from school import db

meta = db.MetaData()

students_groupes = db.Table(
    "students_groupes",
    meta,
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True)
)
