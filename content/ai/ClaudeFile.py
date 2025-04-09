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

    prompt = f"""Please write an HTML blog post for the following {file_type} code. 
    
    Include:
    - Overall purpose and functionality
    - Detailed function/class descriptions
    - Parameters and return values
    - Usage examples
    - Any important notes or considerations

    Here's the code to document:

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


def detect_file_type(file_path):
    """Detect the type of file based on extension."""
    extension = Path(file_path).suffix.lower()
    file_types = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.go': 'Go',
        '.rs': 'Rust',
        '.ts': 'TypeScript',
        '.html': 'HTML',
        '.css': 'CSS',
        '.sql': 'SQL',
    }
    return file_types.get(extension, 'code')


def main():

    parser = argparse.ArgumentParser(description="Generate documentation for code files using Claude API")
    parser.add_argument("file_path", help="Path to the file to document")
    parser.add_argument("--no-save", action="store_true", help="Don't save the documentation to a file")
    parser.add_argument("--output-format", choices=["text", "markdown"], default="markdown", help="Output format for documentation")

    args = parser.parse_args()

    try:

        # Check if file exists
        if not os.path.exists(args.file_path):
            raise FileNotFoundError(f"File not found: {args.file_path}")

        # Read the file
        file_content = read_file(args.file_path)

        # Detect file type
        file_type = detect_file_type(args.file_path)

        print(f"\nGenerating documentation for {file_type} file...")

        # Generate documentation
        documentation = generate_documentation(file_content, file_type)

        # Save documentation if requested
        if not args.no_save:
            doc_path = save_documentation(documentation, args.file_path)
            print(f"\nDocumentation saved to: {doc_path}")

        # Print the documentation
        print("\nGenerated Documentation:\n")
        print(documentation)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
