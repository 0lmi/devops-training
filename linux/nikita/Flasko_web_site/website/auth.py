from flask import Blueprint, render_template, request, flash, redirect
from .db import create_user, get_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", boolean=True)
    elif request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email == "":
            flash('Email must be greater than 3 characters.', category='error')
            return render_template("login.html", boolean=True)
        if password == "":
            flash('Password cannot be empty.', category='error')
            return render_template("login.html", boolean=True)
        
        user = get_user(email)

        if user == None:
            flash('User dosent exist.', category='error')
            return render_template("login.html", boolean=True)
        if password != user['password']:
            flash('Passwords is not valid.', category='error')
            return render_template("login.html", boolean=True)
        
    flash('Successfully logged in', category='success')
    return redirect("/")



@auth.route('/logout')

def logout():
    return redirect("/login")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #if request.method == 'GET':
    #    return render_template("sign_up.html")
    if request.method == 'POST':
        email = request.form.get('email',)
        first_name = request.form.get('first_name',)
        password1 = request.form.get('password1',)
        password2 = request.form.get('password2',)
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        
        create_user(email, first_name, password1)
        flash('Account created!', category='success')
    
        print("True")
        #return render_template("login.html")
    
    #print(request.method)
    print("False")
    return render_template("sign_up.html")