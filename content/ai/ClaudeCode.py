from anthropic import Anthropic
import argparse
from pathlib import Path

import configparser
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

api_key=config['claude']['api_key']


def generate_python_code(prompt):
    """
    Generate Python code using Anthropic's Claude API based on a given prompt.
    
    Args:
        prompt (str): A description of the Python code to generate
    
    Returns:
        str: Generated Python code
    """
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

def save_python_file(code, filename='generated_code.py'):
    """
    Save the generated Python code to a file.
    
    Args:
        code (str): Python code to save
        filename (str, optional): Name of the file to save. Defaults to 'generated_code.py'
    """
    if code:
        with open(filename, 'w') as file:
            file.write(code)
        print(f"Code saved to {filename}")
    else:
        print("No code to save.")

def main(prompt):

    # Example usage
    # prompt = "Create a simple web scraper that fetches the titles of top posts from Reddit"
    
    # Generate Python code
    generated_code = generate_python_code(prompt)
    
    # Save the generated code to a file
    if generated_code:
        save_python_file(generated_code)

if __name__ == "__main__":
    main()
