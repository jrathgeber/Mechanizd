import openai
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

# Set up your OpenAI API key
openai.api_key = config['openai']['api_key']

# Path to the code file you want to document
code_file_path = "C:\\Users\\jrath\\PycharmProjects\\Mechanizd\\content\\ai\\Claude.py"


# Ensure compatibility with openai>=1.0.0
if int(openai.__version__.split('.')[0]) < 1:
    raise ImportError("This script requires openai version >= 1.0.0")


# Function to read the content of the code file
def read_code_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Function to generate documentation using OpenAI API
def generate_documentation(code_content):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a technical writer generating documentation."},
            {"role": "user",
             "content": f"Create a blog post that documents and provides a tutorial for the following code:\n\n{code_content}"}
        ],
        max_tokens=1000,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()


# Main execution
if __name__ == "__main__":
    code_content = read_code_file(code_file_path)
    documentation = generate_documentation(code_content)

    # Save the generated documentation as a blog post
    with open("generated_blog_post.md", "w") as doc_file:
        doc_file.write(documentation)

    print("Documentation successfully generated and saved as 'generated_blog_post.md'")
