from flask import Blueprint, render_template, request, redirect, url_for, flash
#from your_app import db  # Import the database instance if you're using one

auth = Blueprint('auth', __name__)

def token():
    # Handle token logic here
    # get random 11 digits
    token = random.randint(10000000000, 99999999999)

    #c

@auth.route('/login', methods=['GET', 'POST'])
def login():
   
    return 'Login, Page!'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        flash('Account created', 'success')
        return redirect(url_for('auth.login'))  # Redirect to the login page

@auth.route('/logout')
def logout():
    # Handle logout logic here
    return 'user logged out'