from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'what is working'
    #return aip.tell_me_the_future()

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'