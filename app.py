import git
from flask import Flask, request
from routes.auth import auth
from config.dbconnect import mysql

app = Flask(__name__)
app.register_blueprint(auth)

# Enable debug mode
app.debug = True

# Make a CI/CD pipeline to get around PythonAnywhere restrictions
@app.route('/update_server', methods=['POST'])
def webhook():
    try:
        # If the method isn't POST, return an error
        if request.method != 'POST':
            return 'Wrong event type', 400

        # Open the local Git repository
        repo_path = '/home/Xander/Grade-Rescue-backend'  # server local repository path
        repo = git.Repo(repo_path)

        # Pull the latest changes from the git remote
        if 'origin' not in [remote.name for remote in repo.remotes]:
            return 'Remote "origin" does not exist', 400


        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    except Exception as e:
        return f'Error: {str(e)}', 500

# Home route
@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
