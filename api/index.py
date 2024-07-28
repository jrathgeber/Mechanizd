from flask import Flask

import demo2 as aip

app = Flask(__name__)

@app.route('/')
def home():
    return aip.tell_me_the_future()

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'