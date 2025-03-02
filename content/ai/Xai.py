from openai import OpenAI
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

client = OpenAI(
    # This is the default and can be omitted
    api_key=config['Xai']['api_key'],
    base_url="https://api.x.ai/v1"
)

#client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

response = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
     #  {"role": "system", "content": "Be precise and concise."},
        {"role": "user", "content": "What is today's most viral tweet?"}
    ]
)

print(response)