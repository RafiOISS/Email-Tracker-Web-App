from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import db
from app.routes import app as routes_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register routes
    app.register_blueprint(routes_blueprint)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
