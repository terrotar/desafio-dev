from flask import Flask

from .config import db, UPLOAD_FOLDER, SECRET_KEY

from .blueprints.home.routes import home


def create_app(config):

    app = Flask(__name__)

    # os.urandom(12)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)

    # Blueprints
    app.register_blueprint(home)

    with app.app_context():
        db.create_all()

    return app
