import os
import anthropic
import argparse
from pathlib import Path

import configparser
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

api_key=config['claude']['api_key']


def read_file(file_path):

    """Read the contents of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def generate_documentation(file_content, file_type):

    """Generate documentation using Claude API."""
    client = anthropic.Client(api_key=api_key)

    prompt = f"""
        
    Can you take the text in this file and find some great quotes in it. 
       
    Include:
    - the ones where he says first "that's a bar write that down."
    - Other Notable Quotes


    Here's the file to read:

    {file_content}
    """

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return message.content[0].text


def save_documentation(documentation, original_file_path):
    """Save the documentation to a file."""
    # Create filename for documentation
    original_path = Path(original_file_path)
    doc_filename = f"{original_path.stem}_documentation{original_path.suffix}"
    doc_path = original_path.parent / doc_filename

    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(documentation)

    return doc_path


def main(file_path):

    try:

        # Read the file
        file_content = read_file(file_path)

        # Generate documentation
        documentation = generate_documentation(file_content, ".txt")

        # Save documentation if requested
        doc_path = save_documentation(documentation, "C:\\dep\\Mechanizd\\content\\zTemp\\")
        print(f"\nDocumentation saved to: {doc_path}")

        # Print the documentation
        print("\nGenerated Documentation:\n")
        print(documentation)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main("C:\\dep\\Mechanizd\\content\\zTemp\\thats_a_bar.txt")
