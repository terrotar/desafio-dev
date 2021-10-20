from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


UPLOAD_FOLDER = './uploads'

SECRET_KEY = "<F#GK\x92s\xb1\xbf\xf6\xa17"

db = SQLAlchemy()

login_manager = LoginManager()
