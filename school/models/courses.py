from __init__ import db


class course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Course {self.title}>"

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}

