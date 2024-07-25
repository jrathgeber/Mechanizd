import os
from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

# Load environment variables
load_dotenv(find_dotenv())

# Getting the API keys from the .env file
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Langsmith Tracing
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# Fire Crawl API
os.environ['FIRE_API_KEY'] = os.getenv('FIRE_API_KEY')

# Initialize the OpenAI LLM
llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Example 1: Text Generation
prompt = PromptTemplate(input_variables=["topic"], template="Write a short story about {topic}.")
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("a brave knight"))

# Example 2: Text Summarization
text = """
LangChain is a framework for developing applications powered by language models. It enables developers to chain together different components to create sophisticated applications. LangChain provides modules for text generation, summarization, question answering, and more.
"""
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(text)
loader = TextLoader(texts)
documents = loader.load()
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
qa_chain = load_qa_chain(llm, chain_type="map_reduce")
query = "What is LangChain?"
print(qa_chain.run(input_documents=documents, question=query))
