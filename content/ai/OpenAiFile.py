import openai
import os
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')


# Set your OpenAI API key
openai.api_key = config['openai']['api_key']

def upload_file_and_request_documentation(file_path):
    """
    Uploads a file to OpenAI and requests documentation for it.

    Args:
        file_path (str): The path to the file to upload.

    Returns:
        str: The content of the file documentation, if successful, None otherwise.
    """
    try:
        # Upload the file
        with open(file_path, "rb") as file:
            response = openai.files.create(file=file, purpose="assistants")
        file_id = response.id
        # Create an assistant
        assistant = openai.beta.assistants.create(
            name="Documentor",
            instructions="You are a helpful assistant that documents files.",
            tools=[{"type": "file_search"}],
            model="gpt-4-1106-preview"#,
          #  file_ids=[file_id]
        )
        # Create a thread
        thread = openai.beta.threads.create()
        # Add a message to the thread to request documentation
        message = openai.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"Please document the file with id {file_id}.",
            file_ids=[file_id]
        )
        # Run the assistant
        run = openai.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        # Wait for the run to complete
        while run.status != "completed":
            run = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        # Get the assistant's reply
        messages = openai.beta.threads.messages.list(thread_id=thread.id)
        documentation = messages.data[0].content[0].text.value
        return documentation
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = "C:\\Users\\jrath\\PycharmProjects\\Mechanizd\\content\\ai\\Claude.py" # Replace with the actual path to your file

# Create the file if it does not exist
with open(file_path, "w") as f:
    f.write("This is an example file.")

documentation = upload_file_and_request_documentation(file_path)

if documentation:
    print(documentation)
else:
    print("Failed to generate documentation.")