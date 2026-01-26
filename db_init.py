import click
from flask import g
from __init__  import db


def get_db():
    if "db" not in g:
        g.db = db
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.session.close()


def init_db():
    db = get_db()
    db.create_all()
    click.echo("Database initialized")


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Database initialized")


def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
