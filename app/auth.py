from flask import Blueprint,render_template


auth = Blueprint = Blueprint('auth',__name__)


@auth.route('/login')
def login():
    return ('auth/login.html')

@auth.route('logout')
def logout():
    return '<p>Logout</p>'

@auth.route('sign-up')
def signup():
    return ('auth/sign_up.html')



