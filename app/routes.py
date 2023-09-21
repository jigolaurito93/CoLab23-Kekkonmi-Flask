# (from the app folder, import the instance of app inside the init.py file)
from app import app
# Import the render_template module from flask
from flask import render_template, redirect, url_for, flash
# import fake posts form fake data
from fake_data import posts
# import the signup form from forms.py
from app.forms import SignUpForm, LoginForm

# Create a decorator
@app.route('/') #127.0.0.1:5000/
def index():
    # Renders the index.html file
    # Takes 2 arguments, the name of the template AND the variables you want to pass to the template engine as keyword argument arguments
    return render_template('index.html', posts=posts)

@app.route('/signup', methods=['GET', "POST"]) #127.0.0.1:5000/signup
def signup():
    # Create an instance of SignUpForm()
    # Import SignUpForm from app.forms
    form = SignUpForm()

    # If sign up is successful and all are fields are valid
    if form.validate_on_submit():
        # If successful, extract the data from the form fields
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # Flashes an alert message
        # Accessed on the next request ('index')
        # Import flash in flask module
        flash(f"Thank you {first_name} for signing up", 'success')
        
        # If successful, redirect to the specified page
        # Call in the function (index)
        # Import url_for and redirect from flask
        return redirect(url_for('index'))
    
    # If sign up is unsuccessful
    else:
        print('did not valudate')
    # Pass that form as a variable named form
    return render_template('signup.html', form=form)

@app.route('/login') #127.0.0.1:5000/login
def login():
    # Create an instance of login form
    # Import LoginForm from app.forms
    form = LoginForm()


    return render_template('login.html', form=form)