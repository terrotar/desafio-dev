from flask import Blueprint, redirect, render_template, request

from flask_login import login_user, logout_user

from app.models.user import User


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
        user = User.query.filter_by(email=email).first()
        if(not user or not user.verify_password(password)):
            return render_template('login.html',
                                   error=True)
        else:
            login_user(user)
            return redirect('/')
    return render_template('login.html')


# logout
@login.route('/logout', methods=['GET'])
def logout():
    if (request.method == 'GET'):
        logout_user()
        return redirect('/')
