from flask import Blueprint, render_template

bp_home = Blueprint("home_view", __name__, url_prefix="/")


@bp_home.route("/")
@bp_home.route("/home")
def home_page():
    return "Salam Alaykom"
