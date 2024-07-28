from flask import Flask
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    client = OpenAI()
    return 'Is this working?'
    #return aip.tell_me_the_future()

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'