# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def tell_me_the_future():

    # Load environment variables from .env
    load_dotenv()

    # Create a ChatOpenAI model
    model = ChatOpenAI(model="gpt-4o")

    # Invoke the model with a message
    result = model.invoke("Give me a stern warning about the dangers of AI taking over the world.")

    return result.content

if __name__ == '__main__':
    future = tell_me_the_future()
    print(future)