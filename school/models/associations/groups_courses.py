from school import db

meta = db.MetaData()

groups_course = db.Table(
    "groups_course",
    meta,
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True)
)