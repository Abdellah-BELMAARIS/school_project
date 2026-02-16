from school import db


groups_teacher = db.Table(
    "groups_teacher",
    db.metadata,
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True),
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.id"), primary_key=True)
)
