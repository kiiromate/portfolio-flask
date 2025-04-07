from flask import Blueprint, render_template, abort
from app.models.projects import Project

bp = Blueprint('projects', __name__)

@bp.route('/')
def index():
    projects = Project.query.order_by(Project.date.desc()).all()
    return render_template('projects/index.html', projects=projects)

@bp.route('/<slug>')
def view(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    return render_template('projects/view.html', project=project)