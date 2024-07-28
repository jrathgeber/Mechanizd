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
             "content": "You are a computer journalist."},
            {"role": "user", "content": "Create a blog post to highlight a known feature of langchain as a post. "
                                        "Format the output at HTML.(don't suround content with '''html)"}
        ]
    )
    result = completion.choices[0].message.content
    print(result)
    return result

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'