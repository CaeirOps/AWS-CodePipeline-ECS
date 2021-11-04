# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('hello.html')  # return a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'live-lomba' or request.form['password'] != 'xablau':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('login_ok'))
    return render_template('login.html', error=error)

@app.route('/login-ok')
def login_ok():
    return render_template("login-ok.html")  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
