# Import the Flask application
from flask import Flask

# Create instance of Flask class with the name "app"
app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess-this'

# import all of the routes from the routes.py file into the current package
# (from the current directory, import routes.py)
from . import routes














# If youre running the script, then run the application
# if __name__ == '__main__':
#     app.run()
    # app.run(debug=True)


