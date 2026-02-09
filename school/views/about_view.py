from flask import Blueprint, render_template

bp_about = Blueprint("about_view", __name__, url_prefix="/about")


@bp_about.route("/about")
def about_page():
    return render_template("about.html")
