from flask import Blueprint,render_template,request


auth = Blueprint = Blueprint('auth',__name__)


@auth.route('/login',methods =['GET','POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


    return render_template('auth/sign_up.html')



