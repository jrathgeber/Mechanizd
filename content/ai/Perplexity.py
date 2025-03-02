from openai import OpenAI
import configparser


# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

client = OpenAI(
    # This is the default and can be omitted
    api_key=config['perplexity']['api_key'],
    base_url="https://api.perplexity.ai"
)

#client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

response = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {"role": "system", "content": "Be precise and concise."},
        {"role": "user", "content": "How many stars are there in our galaxy?"}
    ]
)

print(response)