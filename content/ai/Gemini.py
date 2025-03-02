import google.generativeai as genai
import configparser


def generate_article(model_name, prompt):
    """
    Generates an article using the Gemini API.

    Args:
        model_name: The name of the Gemini model to use (e.g., "gemini-1.0-pro").
        prompt: The prompt for the article generation.

    Returns:
        The generated article text, or None if an error occurs.
    """

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    api_key = config['gemini']['api_key']

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating article: {e}")
        return None


if __name__ == "__main__":

    model_name = "gemini-2.0-flash"
    prompt = "Write a short article about the benefits of walking for 30 minutes a day."

    article = generate_article(model_name, prompt)

    if article:
        print(article)
