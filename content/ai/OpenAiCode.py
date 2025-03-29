from openai import OpenAI
import re

import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

client = OpenAI(
    # This is the default and can be omitted
    api_key=config['openai']['api_key'],
)

# Call OpenAI API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an AI that strictly outputs only valid Python code without any explanations, comments, or markdown formatting."},
        {"role": "user", "content": "Write a Python program that prints 'Hello, World!'."}
            ]


)

# Extract the message content
text_response = response.choices[0].message.content

# Extract code using regex
match = re.search(r"```python\n(.*?)```", text_response, re.DOTALL)
python_code = match.group(1) if match else text_response  # If no backticks, use full text

# Save to a Python file
with open("output.py", "w") as file:
    file.write(python_code)

print("Python code saved as output.py")