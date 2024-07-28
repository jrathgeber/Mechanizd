# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from openai import OpenAI

def tell_me_the_future():

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are a fear mongering pessimist."},
            {"role": "user", "content": "Create a warning about the dangers of AI."}
        ]
    )

    print(completion.choices[0].message)

    # Invoke the model with a message
    result = completion.choices[0].message

    return result.content

if __name__ == '__main__':
    future = tell_me_the_future()
    print(future)