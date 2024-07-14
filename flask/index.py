from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to Mechanizd Time Series ML.</p>"