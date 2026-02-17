from flask import Blueprint, render_template
from flask_login import login_required

bp_about = Blueprint("about_view", __name__, url_prefix="/about")

@bp_about.route("/about")
def about_page():
    return render_template("about.html")

@bp_about.route('/dashboard')
@login_required
def dashboard_page():
    return render_template('dashboard.html')