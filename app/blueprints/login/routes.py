from flask import Blueprint, redirect, render_template, request

from flask_login import current_user, login_user, logout_user

from app.models.user import User

from app.config import db


# Instance of Blueprint login
login = Blueprint('login', __name__,
                  template_folder="templates",
                  static_folder="static")


# login
@login.route('/login', methods=['GET', 'POST'])
def log_user():
    if(request.method == 'POST'):
        email = request.form['email']
        password = request.form['pwd']

        # Check if exists an user with same email and verify password
        user = User.query.filter_by(email=email).first()
        if(not user or not user.verify_password(password)):
            return render_template('login/login.html',
                                   error=True)

        else:
            login_user(user)
            return redirect('/')
    return render_template('login/login.html')


# logout
@login.route('/logout', methods=['GET'])
def logout():
    if (request.method == 'GET'):
        logout_user()
        return redirect('/')


# Profile
@login.route('/profile', methods=['GET'])
def profile():
    if(request.method == 'GET'):
        return render_template('login/profile.html')


# Change password
@login.route('/change/pwd', methods=['GET', 'POST'])
def change_pwd():
    user = User.query.get(current_user.id)
    if(request.method == 'GET'):
        if(user):
            return render_template('login/change_pwd.html')
    elif(request.method == 'POST'):
        old_pwd = request.form['old_pwd']
        new_pwd = request.form['new_pwd']

        # Verify password of current_user
        if(not user.verify_password(old_pwd)):
            return render_template('login/change_pwd.html',
                                   pwd_error=True)

        # Change the new password
        else:
            user.password = new_pwd
            db.session.commit()
            logout_user()
            return render_template('index.html')
    return render_template('login/profile.html')


# Change Data
@login.route('/change/data', methods=['GET', 'POST'])
def change_data():
    user = User.query.get(current_user.id)
    if(request.method == 'GET'):
        if(user):
            return render_template('login/change_data.html')
        else:
            return redirect('/')
    elif(request.method == 'POST'):
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        pwd = request.form['pwd']

        # Verify password of current_user
        if(not user.verify_password(pwd)):
            return render_template('login/change_data.html',
                                   pwd_error=True)

        # Change the new data
        else:
            user.email = email
            user.fname = fname
            user.lname = lname
            db.session.commit()
            logout_user()
            return redirect('/')
    return render_template('login/profile.html')
