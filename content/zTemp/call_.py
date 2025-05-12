import requests
import json

API_KEY = "your_api_key_here"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_grok(question):
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are Grok, an AI assistant created by xAI."},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
    response_json = response.json()

    if response.status_code == 200:
        return response_json['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response_json['error']['message']}"

question = "What is the meaning of life?"
answer = ask_grok(question)
print(f"Question: {question}")
print(f"Grok's answer: {answer}")