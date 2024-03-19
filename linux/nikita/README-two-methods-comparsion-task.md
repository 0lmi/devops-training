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

### Last line in Function 2 going to be run, for POST request?

Yes its going to be run for POST request and for GET request.
 
### Is those two function working same principle or not?

Yes this two functions is working by the same principle.

### Explain your answer:

Example of simple if statement with only 1 test expression:

```

x = 5
b = 10

def real_one():
    
    if x < b:
        print ("Condition is true")

print ("The planet are circle")

```
Output will be:
Condition is true
The planet are circle

This happening because of statement was running by the plan.
- Test expression
- Body of if statement (Our code block)
- Statement just below if (Outside the code block)

In test if statement, condition will always going to be *true*, because x variable is lower than b variable.
Thats why output is print that *condition is true*.
Then output shows for us that planet are circle, it was printing not because statement is true.
But its print only because it was just below the if, for statement its dosent matter if condition going to be *True* or *False*, it will run last command anyway.

---
### Let`s go back to our sheep

*Function 1*
We have 2 statement where stricted writted what *POST* and *GET* requests should to do

*Function 2*
Have only 1 statement where only writted what *POST* should to do, but its going to work anyway.
Because last line is working for 2 request, when we getting *POST* and *GET* requests.
Again how im showed in *test function*, for statement its dosent matter when it need to run last command which are outside the code block, when its *False* or *True*.
It will run it anyway.

In my opinion *Function 2* writted more correctly and greater, because it making easier job for flask.
