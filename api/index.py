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
            {"role": "user", "content": "Create a quick short warning about AI taking over the word. Format the output at HTML."}
        ]
    )
    result = completion.choices[0].message.content
    print(result)
    return result

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'