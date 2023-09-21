# (from the app folder, import the instance of app inside the init.py file)
from app import app
# Import the render_template module from flask
from flask import render_template
# import fake posts form fake data
from fake_data import posts

# Create a decorator
@app.route('/') #127.0.0.1:5000/
def index():
    # Renders the index.html file
    # Takes 2 arguments, the name of the template AND the variables you want to pass to the template engine as keyword argument arguments
    return render_template('index.html', posts=posts)

@app.route('/signup') #127.0.0.1:5000/signup
def signup():
    return render_template('signup.html')

@app.route('/login') #127.0.0.1:5000/login
def login():
    return render_template('login.html')