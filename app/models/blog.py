from app import db
from datetime import datetime
from slugify import slugify

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        super(BlogPost, self).__init__(*args, **kwargs)