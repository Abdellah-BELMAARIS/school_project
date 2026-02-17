from school import db
from school.data.classes_data import (
    p_grade_1,
    p_grade_2,
    p_grade_3,
    p_grade_4,
    p_grade_5,
    p_grade_6,
)
from school.data.courses_data import math, arabic, history_geography
from school.data.groups_data import p_groups, c_groups, h_groups
from school.data.parents_data import parent1, parent2, parent3
from school.data.students_data import student1, student2, student3
from school.data.teachers_data import teacher1, teacher2, teacher3


def insert_database():
    db.session.add_all([parent1, parent2, parent3])

    db.session.add_all(
        [p_grade_1, p_grade_2, p_grade_3, p_grade_4, p_grade_5, p_grade_6]
    )

    for group in p_groups + c_groups + h_groups:
        group.school_class = p_grade_1

    db.session.add_all(p_groups + c_groups + h_groups)

    math.school_class = p_grade_1
    arabic.school_class = p_grade_1
    history_geography.school_class = p_grade_1

    db.session.add_all([math, arabic, history_geography])

    student1.parent = parent1
    student1.school_class = p_grade_1

    student2.parent = parent1
    student2.school_class = p_grade_2

    student3.parent = parent3
    student3.school_class = p_grade_3

    db.session.add_all([student1, student2, student3])

    teacher1.school_class = p_grade_1
    teacher1.course = math
    teacher1.groups.append(p_groups[0])

    teacher2.school_class = p_grade_1
    teacher2.course = arabic

    teacher3.school_class = p_grade_2
    teacher3.course = history_geography

    db.session.add_all([teacher1, teacher2, teacher3])

    student1.class_courses.extend([math, arabic])
    student2.class_courses.append(arabic)
    student3.class_courses.append(history_geography)

    p_groups[0].courses.extend([math, arabic])
    c_groups[0].courses.append(history_geography)

    p_grade_1.class_courses.extend([math, arabic])
    p_grade_2.class_courses.append(history_geography)

    db.session.commit()

    print("Database created successfully!")

if __name__ == "__main__":
    from school import create_app
    
    app = create_app()
    with app.app_context():
        print("Inserting data...")
        insert_database()
