import openai

import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

openai.organization = config['openai']['api_org']
openai.api_key = config['openai']['api_key']
#openai.Model.list()

text = "Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English. We are open-sourcing models and inference code to serve as a foundation for building useful applications and for further research on robust speech processing."
response = openai.Completion.create(
  engine="davinci-002",
  prompt=f"Tweetify:\n{text}",
  max_tokens=50
)

summary = response.choices[0].text.strip()
print(summary)