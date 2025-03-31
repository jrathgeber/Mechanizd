from openai import OpenAI
import configparser
import prompts.aGainers as gain_prompt


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

    prompt = gain_prompt.get_prompt(tick_list)

    # prompt = "Provide super concise info about the following stocks. If a stock can't be found just ignore it and say nothing. Don't provide citation or citation numbers. Don't introduce the list just get to the stocks : " + tick_list

    print("\n The Gainers prompt : \n" + prompt)

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "system", "content": "You are a stock research expert"},
            {"role": "user", "content": prompt}
        ]
    )

    print(f"From perplexity : {response}")
    return response.choices[0].message.content


def get_stock_info(tick_list):

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=config['perplexity']['api_key'],
        base_url="https://api.perplexity.ai"
    )

    print(tick_list)

    prompt = "Provide some info about this stock : " + tick_list

    print("\nFurther details : \n" + prompt)

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "system", "content": "You are an equity research expert"},
            {"role": "user", "content": prompt}
        ]
    )

    print(f"From perplexity : {response}")
    return response.choices[0].message.content