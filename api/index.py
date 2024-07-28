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
             "content": "You are an AI blogger."},
            {"role": "user", "content": "Create a short blog post to highlight a known feature of langchain as a post. Include one code block. Format the output at HTML. Don't surround content with '''html)"}
        ]
    )
    result = completion.choices[0].message.content
    print(result)
    return result

@app.route('/about')
def about():
    return 'Developed by Jason Rathgeber'