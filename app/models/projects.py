from app import db
from datetime import datetime
from slugify import slugify

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    short_description = db.Column(db.String(200))
    image = db.Column(db.String(200))
    technologies = db.Column(db.String(200))  # Comma-separated list
    github_link = db.Column(db.String(200))
    live_link = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    featured = db.Column(db.Boolean, default=False)
    color = db.Column(db.String(20), default="#3B82F6")  # For visual elements
    
    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        super(Project, self).__init__(*args, **kwargs)