from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from config.dbconnect import mydb
from access_token import generate_access_token, token_destroy, token_validate

auth = Blueprint('auth', __name__)
app = Flask(__name__)

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    mydb.start_transaction()
    cursor = mydb.cursor(dictionary=True)

    # Check if the user exists (You should replace this with database queries)
    cursor.execute("SELECT * FROM students WHERE username = %s AND password = %s", (username, password))
    
    user = cursor.fetchone()

    if user:
        # destroy all tokens for this user
        response = token_destroy(user.id)
      

        # Generate a new access token
        access_token = generate_access_token(user.id)

        # Return the access token and user's complete details
        user_details = {
            'user_id': user.id,
            'username': user.username,
            'first_name': user.firstName,
            'last_name': user.lastName,
        }

        return jsonify({'access_token': access_token, 'user': user_details}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_type = data.get('user_type')  # Identify whether it's a student or instructor registration
    username = data.get('username')
    password = data.get('password')

    # Additional user details
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    gender = data.get('gender')
    phone = data.get('phone')
    email = data.get('email')
    telegram_id = data.get('telegram_id')
    faculty = data.get('faculty')
    department = data.get('department')
    disciplinary_status = data.get('disciplinary_status')
    current_semester = data.get('current_semester')

    if not username or not password:
        return jsonify({'message': 'Both username and password are required'}), 400

    cursor = mydb.cursor(dictionary=True)  # Create a cursor that returns results as dictionaries

    try:
        # Begin a transaction
        mydb.start_transaction()

        # Insert the new user (student or instructor) into the respective table
        if user_type == 'student':
            cursor.execute(
                "INSERT INTO students (FirstName, LastName, Gender, Phone, Email, TelegramID, Faculty, Department, DisciplinaryStatus, CurrentSemester, username, password) "
                "VALUES (%(first_name)s, %(last_name)s, %(gender)s, %(phone)s, %(email)s, %(telegram_id)s, %(faculty)s, %(department)s, %(disciplinary_status)s, %(current_semester)s, %(username)s, %(password)s)",
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'phone': phone,
                    'email': email,
                    'telegram_id': telegram_id,
                    'faculty': faculty,
                    'department': department,
                    'disciplinary_status': disciplinary_status,
                    'current_semester': current_semester,
                    'username': username,
                    'password': password,
                }
            )
        elif user_type == 'instructor':
            cursor.execute(
                "INSERT INTO instructors (FirstName, LastName, Gender, Phone, Email, TelegramID, Faculty, Department, DisciplinaryStatus, CurrentSemester, username, password) "
                "VALUES (%(first_name)s, %(last_name)s, %(gender)s, %(phone)s, %(email)s, %(telegram_id)s, %(faculty)s, %(department)s, %(disciplinary_status)s, %(current_semester)s, %(username)s, %(password)s)",
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'phone': phone,
                    'email': email,
                    'telegram_id': telegram_id,
                    'faculty': faculty,
                    'department': department,
                    'disciplinary_status': disciplinary_status,
                    'current_semester': current_semester,
                    'username': username,
                    'password': password,
                }
            )
        else:
            return jsonify({'message': 'Invalid user type'}), 400

        # Get the ID of the newly inserted user
        cursor.execute("SELECT LAST_INSERT_ID()")
        user_id = cursor.fetchone()['LAST_INSERT_ID()']

        # Generate and store the access token
        access_token = generate_access_token()
        cursor.execute("INSERT INTO personal_access_tokens (user_id, token) VALUES (%s, %s)", (user_id, access_token))

        # Commit the transaction
        mydb.commit()
    except Exception as e:
        # Rollback the transaction if an error occurs
        mydb.rollback()
        return jsonify({'message': 'Error occurred during registration'}), 500
    finally:
        cursor.close()

    return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201


@auth.route('/logout')
def logout():
    # destroy all tokens for this user
    response = token_destroy(user_id)

    return jsonify('user logged out')