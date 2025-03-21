from openai import OpenAI
import configparser
import content.prompts.Gainers1 as gain_prompt


def get_latest_info(prompt):

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=config['perplexity']['api_key'],
        base_url="https://api.perplexity.ai"
    )

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "system", "content": "Be precise and concise."},
            {"role": "user", "content": prompt}
        ]
    )

    print(f"From perplexity : {response}")
    return response.choices[0].message.content


def get_gainers_info(tick_list):

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=config['perplexity']['api_key'],
        base_url="https://api.perplexity.ai"
    )

    print(tick_list)

    prompt = "Write a short research report about each of these stocks : " + tick_list

    print("\nFurther details : \n" + prompt)

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "system", "content": "You are a stock research expert"},
            {"role": "user", "content": prompt}
        ]
    )

    print(f"From perplexity : {response}")
    return response.choices[0].message.content