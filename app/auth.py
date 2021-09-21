from flask import Blueprint,render_template,request,flash


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

        if len(email) < 8:
            flash('Email must be greater than 8 characters', category='error')
        elif len(firstName) < 2:
            flash('Name must greater than 2 characters', category='error')
        if password1 != password2:
            flash('Passwords don\'t match ', category='error')
        # elif len(password1)<7:
        #     flash('password must be atleast  7 characters', category='error')
        else:
            # add user to database
            flash('Account created succefully',category='success')
              





    return render_template('auth/sign_up.html')



