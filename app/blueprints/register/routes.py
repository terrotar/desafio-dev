from flask import Blueprint, redirect, render_template, request

from flask_login import login_user

from app import db

from app.models.user import User


# Instance of Blueprint register
register = Blueprint('register', __name__,
                     template_folder="templates",
                     static_folder="static")


# register
@register.route('/cadastrar', methods=['GET', 'POST'])
def register_user():
    if(request.method == 'POST'):
        new_user = User(email=request.form['email'],
                        password=request.form['pwd'],
                        fname=request.form['fname'],
                        lname=request.form['lname'])
        email_checker = User.query.filter_by(email=request.form['email']).first()
        if email_checker:
            return render_template('register.html',
                                   email_error=True)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return render_template('index.html')
    return render_template('register.html')
