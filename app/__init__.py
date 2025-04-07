from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.routes.projects import bp as projects_bp
    app.register_blueprint(projects_bp, url_prefix='/projects')
    
    from app.routes.blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')
    
    return app