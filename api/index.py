from flask import Flask
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are a fear mongering pessimist."},
            {"role": "user", "content": "Create a warning about the dangers of AI."}
        ]
    )
    result = completion.choices[0].message.content
    return result

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'