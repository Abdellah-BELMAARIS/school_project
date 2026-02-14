from school import create_app, db
from school.models.associations import school_class_course
from school.data.classes_data import primary_class, college_class, high_school_class


app = create_app()

with app.app_context():
    db.create_all()

    db.session.add(primary_class)
    db.session.add(college_class)
    db.session.add(high_school_class)

    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
