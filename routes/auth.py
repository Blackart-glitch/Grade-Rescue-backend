from flask import Blueprint, render_template, request, redirect, url_for, flash
#from your_app import db  # Import the database instance if you're using one

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
   
    return 'Login, Page!'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        flash('Account created', 'success')
        return redirect(url_for('auth.login'))  # Redirect to the login page
