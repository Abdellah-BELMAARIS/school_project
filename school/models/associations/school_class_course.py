from school import db

metadata = db.metadata

school_class_course = db.Table(
    "school_class_course",
    metadata,
    db.Column("school_class_id", db.Integer, db.ForeignKey("school_classes.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True)
)