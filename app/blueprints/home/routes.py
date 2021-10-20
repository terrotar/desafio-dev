from flask import Blueprint, redirect, render_template, request

# Rename the file's name into a secure pattern
from werkzeug.utils import secure_filename

from ...config import UPLOAD_FOLDER

import os

from loguru import logger


# Instance of Blueprint home
home = Blueprint('home', __name__,
                 template_folder="templates",
                 static_folder="static")


# homepage
@home.route('/', methods=['GET'])
def index():
    if(request.method == 'GET'):
        return render_template('index.html')


# upload file
@home.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if(request.method == 'POST'):
        file = request.files['file']
        if(file):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return "Uploaded file with sucess."
    return redirect('/')
