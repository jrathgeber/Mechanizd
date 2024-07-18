from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Mechanizd Python API is where it is at.'

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'