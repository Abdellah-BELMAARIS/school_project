from __init__ import db

class teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Teacher {self.name}, Subject: {self.subject}, Email: {self.email}>"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "subject": self.subject, "email": self.email}
    