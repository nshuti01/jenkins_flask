# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import datetime

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error, datetime_now=datetime.datetime.now())


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=6060)#, ssl_context="adhoc"