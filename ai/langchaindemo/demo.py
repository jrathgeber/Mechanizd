import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # important line if cannot load api key

## Getting the api keys from the .env file

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Langsmith Tracing
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# Fire Crawl API
os.environ['FIRE_API_KEY']=os.getenv('FIRE_API_KEY')