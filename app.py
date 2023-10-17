from flask import Flask
from routes.auth import auth

app = Flask(__name__)
app.register_blueprint(auth)

# Enable debug mode
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
