from app import create_app, db
from app.models.projects import Project
from app.models.blog import BlogPost
from flask_migrate import Migrate
import click

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    """Make database models available in Flask shell."""
    return {
        'db': db,
        'Project': Project,
        'Post': BlogPost
    }

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
@click.argument('username')
@click.argument('password')
def create_admin(username, password):
    """Create an admin user."""
    from app.models.user import User
    user = User(username=username, is_admin=True)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    click.echo(f'Created admin user: {username}')

if __name__ == '__main__':
    app.run(debug=True)