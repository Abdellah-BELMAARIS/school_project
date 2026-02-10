from datetime import date
from school import db
from school.models.student_model import StudentDB


student1 = StudentDB(
    first_name="Abdellah",
    last_name="BELMAARIS",
    birthday=date(2010, 7, 19),
    email="obaid@gmail.com",
)

db.session.add(student1)
db.session.commit()
