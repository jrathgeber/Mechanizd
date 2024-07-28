from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'A crew of AIs is really comming.'

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'