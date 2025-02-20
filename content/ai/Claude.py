import os
import anthropic
import argparse
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

api_key=config['claude']['api_key']

def generate_article(topic, length="short"):
    # Initialize the Anthropic client
    client = anthropic.Client(api_key=api_key)

    # Define length parameters
    length_params = {
        "short": "approximately 300 words",
        "medium": "approximately 600 words",
        "long": "approximately 1000 words"
    }

    # Construct the prompt
    prompt = f"""Please write an informative article about {topic}. 
    The article should be {length_params[length]}.
    Use an engaging, professional tone and include relevant details and examples.
    Structure the article with a clear introduction, body paragraphs, and conclusion."""

    # Create the message
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

    # Extract the response
    article = message.content[0].text

    return article

def save_article(article, topic):
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"article_{topic.replace(' ', '_')}_{timestamp}.txt"
    
    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(article)
    
    return filename

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate an article using Claude API")
    parser.add_argument("topic", help="The topic for the article")
    parser.add_argument("--length", choices=["short", "medium", "long"], 
                        default="medium", help="Length of the article")
    parser.add_argument("--save", action="store_true", 
                        help="Save the article to a file")

    args = parser.parse_args()

    try:
        # Check for API key
        # if "ANTHROPIC_API_KEY" not in os.environ:
        #    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable")

        # Generate article
        article = generate_article(args.topic, args.length)
        
        # Save if requested
        if args.save:
            filename = save_article(article, args.topic)
            print(f"\nArticle saved to: {filename}")
        
        # Print the article
        print("\nGenerated Article:\n")
        print(article)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
