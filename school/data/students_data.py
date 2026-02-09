from datetime import date
from school import db
from models import StudentDB


student1 = StudentDB(
    first_name="Abdellh",
    last_name="BELMAARIS",
    birthday=date(2010, 7, 19),
    email="obaid@gmail.com",
)

db.session.add(student1)
db.session.commit()
