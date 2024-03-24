# Two functions examples:

Function 1:
```
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template("sign_up.html")
    elif request.method == 'POST':
        email = request.form.get('email', '')
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

        return render_template("sign_up.html")
```

Function 2:
```
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email', '')
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

    return render_template("sign_up.html")
```
----
### The main question of the task is those two functions are compilation the same principle or not, and describe my answer.
Answer is: Yes those two functions are compilation the same principle.
As we know that GET method will be as defoult method, we need only mark in the code where we doing the *POST* request.
In *Function 1* GET method writted in if statement. 
In *Function 2* GET method is in line 19, outside the *POST* method code block.

In function 1, GET request activates when condition `if request.method == 'GET'` will be true.
In function 2, GET request activates when you passes that link *http://127.0.0.1:5000/sign_up*.

Soo when in both scenarios return render_template("sign_up.html") commands are the same, that making this functions compilating the same principle.
