from flask import Blueprint,render_template


auth = Blueprint = Blueprint('auth',__name__)


@auth.route('/login',methods =['GET','POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    return render_template('auth/sign_up.html')



