from flask_login import login_required
from .about_view import bp_about
from flask import render_template


@bp_about.route('/dashboard')
@login_required
def dashboard_page():
    return render_template('dashboard.html')