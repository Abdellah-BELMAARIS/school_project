from school import create_app, db

app = create_app()

with app.app_context():
    from school.models import (
        CourseDB,
        GroupDB,
        ParentDB,
        HighSchoolClassDB,
        PrimaryClassDB,
        CollegeClassDB,
        StudentDB,
        TeacherDB,
    )

    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
