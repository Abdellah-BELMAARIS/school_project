from school import create_app, db
from school.models import (
    StudentDB,
    ParentDB,
    TeacherDB,
    CourseDB,
    GroupDB,
    PrimaryClassDB,
    CollegeClassDB,
    HighSchoolClassDB,
)

from school.models.associations import (
    school_class_course,
    students_course,
    students_groupes,
    groups_course,
    teachers_course,
    groups_teacher,
)

from school.data import (
    primary_class,
    college_class,
    high_school_class,
    math,
    arabic,
    history_geography,
    p_groups,
    c_groups,
    h_groups,
    parent1,
    parent2,
    parent3,
    student1,
    student2,
    student3,
    teacher1,
    teacher2,
    teacher3,
)


app = create_app()


with app.app_context():
    db.create_all()

    db.session.add_all(
        [
            primary_class,
            college_class,
            high_school_class,
            math,
            arabic,
            history_geography,
            p_groups,
            c_groups,
            h_groups,
            parent1,
            parent2,
            parent3,
            student1,
            student2,
            student3,
            teacher1,
            teacher2,
            teacher3,
        ]
    )

    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
