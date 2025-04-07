from flask import Blueprint, render_template
from app.models.blog import BlogPost

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.date.desc()).all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/<slug>')
def view(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/view.html', post=post)