from school import create_app
from insert_data import insert_database


app = create_app()



if __name__ == "__main__":
    with app.app_context():
        insert_database()
    app.run(debug=True)
