from flask import Flask

from .config import db, login_manager, UPLOAD_FOLDER, SECRET_KEY

# Blueprints
from .blueprints.home.routes import home
from .blueprints.register.routes import register
from .blueprints.login.routes import login

# Models
from .models.user import User
from .models.file import File
from .models.transaction import Transaction
from.models.store import Store


def create_app(config):

    app = Flask(__name__)

    # os.urandom(12)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/bycoders"

    db.init_app(app)

    login_manager.init_app(app)

    # Blueprints
    app.register_blueprint(home)
    app.register_blueprint(register)
    app.register_blueprint(login)

    with app.app_context():
        db.create_all()

    return app
