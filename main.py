from school import create_app, db
from insert_data import insert_database

app = create_app()

with app.app_context():
    # 1. Create all database tables if they don't exist yet
    db.create_all()
    
    # 2. Check if data already exists (looking for a primary class)
    from school.models import PrimaryClassDB
    if not db.session.query(PrimaryClassDB).first():
        insert_database()

if __name__ == "__main__":
    app.run(debug=True)