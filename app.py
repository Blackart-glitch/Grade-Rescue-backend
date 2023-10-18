from flask import Flask, request
from routes.auth import auth
from config.dbconnect import mysql
import git

app = Flask(__name__)
app.register_blueprint(auth)

# Enable debug mode
app.debug = True

# make do CI/CD pipeline to get around pythonanywhere restrictions
@app.route('/update_server', methods=['POST'])
def webhook():
    try:
        #if the method is'nt post, return error
        if request.method != 'POST':
            return 'Wrong event type', 400
        #pull from git
        repo = git.Repo('https://github.com/Blackart-glitch/Grade-Rescue-backend.git')
        origin = repo.remotes.origin
        origin.pull()

        #return to git as payload
        return 'Updated PythonAnywhere successfully', 200
    except Exception as e:
        return f'Error: {str(e)}', 500

# Home route
@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
