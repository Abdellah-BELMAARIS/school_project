from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import path

db = SQLAlchemy()
DB_NAME = "school.db"


def create_app(test_config=None):


    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from views import bp_home, bp_about

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_about)


    with app.app_context():
        db.create_all()


    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
