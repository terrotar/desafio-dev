from flask import Blueprint, redirect, render_template, request


# Instance of Blueprint register
register = Blueprint('register', __name__,
                     template_folder="templates",
                     static_folder="static")


# register
@register.route('/register', methods=['GET'])
def register_user():
    if(request.method == 'GET'):
        return render_template('register.html')
