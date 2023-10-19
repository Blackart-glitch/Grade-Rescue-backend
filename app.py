from flask import Flask, request
from routes.auth import auth
from config.dbconnect import mysql
import subprocess

app = Flask(__name__)
app.register_blueprint(auth)

# Enable debug mode
app.debug = True

# Make a CI/CD pipeline to get around PythonAnywhere restrictions, doesn't work yet

""" @app.route('/update_server', methods=['POST'])
def webhook():
        # If the method isn't POST, return an error
        if request.method != 'POST':
            return 'Wrong event type', 400

        # Run the bash script
        subprocess.run(['bash', 'script.sh'])

        return 'Updated PythonAnywhere successfully', 200 """

# Home route
@app.route('/')
def hello_world():
    return 'Grade Rescue home!'

if __name__ == '__main__':
    app.run()
