from flask import Blueprint, redirect, render_template, request, url_for

from flask_login import current_user

# Rename the file's name into a secure pattern
from werkzeug.utils import secure_filename

# Folder of uploaded files
from ...config import UPLOAD_FOLDER

from app.config import db

from app.models.file import File
from app.models.store import Store

import os


# Instance of Blueprint home
home = Blueprint('home', __name__,
                 template_folder="templates",
                 static_folder="static")


# Allowed extensions of upload files
# To have a new one just insert it in the array below
ALLOWED_EXT = ['csv', 'txt']


# homepage
@home.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'GET'):
        all_stores = Store.query.all()
        return render_template('index.html', all_stores=all_stores)
    if(request.method == 'POST'):
        file = request.files['file']

        # Set a secure filename to the file sent
        filename = secure_filename(file.filename)

        # Check if there's a valid file and extension
        check_ext = filename.split('.')
        if(check_ext[-1] not in ALLOWED_EXT):
            return render_template('index.html', ext_error=True)

        # Save uploaded file inside UPLOAD_FOLDER
        if(file):
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            # Check if already exists that file by it's name
            check_file = File.query.filter_by(filename=filename).first()
            if(check_file):
                return render_template('index.html', upload_error=True)

            # Split saved file by it's values
            doc = open(f"{UPLOAD_FOLDER}/{filename}", "r")
            for line in doc:
                transaction = line[0:1]
                date = line[1:9]
                value = float(line[9:19])/100
                cpf = line[19:30]
                card_number = line[30:42]
                time = line[42:48]
                owner = line[48:62]
                store = line[62:80]

                # Set value into + or - to add in store.balance
                if(transaction == 2) or (transaction == 3) or (transaction == 9):
                    value = -value

                # Check if already exists that store and create if not
                check_store = Store.query.filter_by(name=store).first()
                if(not check_store):
                    new_store = Store(owner=owner,
                                      cpf=cpf,
                                      name=store,
                                      balance=value)
                    db.session.add(new_store)
                    db.session.commit()
                else:
                    check_store.balance += value

                # Get the store.id that already exists and create a File object
                store = Store.query.filter_by(name=store).first()
                doc = File(filename=filename,
                           id_user=current_user.id,
                           id_store=store.id,
                           id_transaction=transaction,
                           date=date,
                           time=time,
                           value=+value,
                           card_number=card_number,)
                db.session.add(doc)
                db.session.commit()
            return render_template('index.html', upload_success=True)
        else:
            # Return of an invalid file
            return render_template('index.html', file_error=True)
    return redirect(url_for('home.index'))
