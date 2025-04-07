from flask import Blueprint

from . import main, projects, blog

def init_app(app):
    app.register_blueprint(main.bp)
    app.register_blueprint(projects.bp, url_prefix='/projects')
    app.register_blueprint(blog.bp, url_prefix='/blog')