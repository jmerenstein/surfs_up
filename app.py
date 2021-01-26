from flask import Flask

# creating new Flask app instance
app = Flask(__name__)

# create Flask route
@app.route('/')
def hello_world():
    return 'Hello world'

