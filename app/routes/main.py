from flask import Blueprint, render_template
from app.models.projects import Project

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    featured_projects = Project.query.filter_by(featured=True).all()
    return render_template('index.html', featured_projects=featured_projects)

@bp.route('/about')
def about():
    return render_template('about.html')