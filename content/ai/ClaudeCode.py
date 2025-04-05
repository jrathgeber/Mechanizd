from anthropic import Anthropic

import configparser
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

api_key = config['claude']['api_key']
code_path = config['blog']['blog_temp']


def generate_python_code(prompt):

    # Initialize the Anthropic client
    # Note: You must set the ANTHROPIC_API_KEY environment variable
    client = Anthropic(api_key=api_key)
    
    try:
        # Create the API request
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            messages=[

                {
                    "role": "user",
                    "content": "You are an AI that strictly outputs only valid Python code"
                               " without any explanations, comments, or markdown formatting."},

                {
                    "role": "user",
                    "content": f"Please generate a complete, runnable Python script for the following task: {prompt}. "
                               "Ensure the code is fully functional and includes necessary imports."
                }
            ]
        )
        
        # Extract the generated code from the response
        generated_code = response.content[0].text
        
        return generated_code
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def hyphen_split(s):
    pos = s.index('_')
    try:
        return s[:s.index('_', pos + 1)]
    except ValueError:
        return s[:pos]



def save_python_file(slug, code):

    print(hyphen_split(slug))

    filename = code_path + hyphen_split(slug) + '.py'

    if code:
        with open(filename, 'w') as file:
            file.write(code)
        print(f"Code saved to {filename}")
    else:
        print("No code to save.")


def write_code_task(prompt):

    slug = prompt.replace(" ", "_")

    # Example usage
    # prompt = "Create a simple web scraper that fetches the titles of top posts from Reddit"
    
    # Generate Python code
    generated_code = generate_python_code(prompt)
    
    # Save the generated code to a file
    if generated_code:
        save_python_file(slug, generated_code)


if __name__ == "__main__":
    write_code_task("Send a message to whatsapp")
