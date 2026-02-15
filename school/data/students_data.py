from datetime import date
from school import db
from models.student_model import StudentDB


student1 = StudentDB(
    first_name="Abdellah",
    last_name="BELMAARIS",
    birthday=date(2010, 7, 19),
    email="obaid@gmail.com",
)

student2 = StudentDB(
    first_name="Sara",
    last_name="BELMAARIS",
    birthday=date(2016, 3, 6),
    email="sara@gmail.com",
)

student3 = StudentDB(
    first_name="Omar",
    last_name="AlAOUI",
    birthday=date(2005, 11, 22),
    email="omar@gmail.com",
)

