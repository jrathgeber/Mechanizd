'''

Here's a complete, runnable Python script that demonstrates how to upload a post to Beehiiv using their API. Please note that you'll need to replace 'YOUR_API_KEY' with your actual Beehiiv API key:

python

'''

import requests
import json


def upload_post_to_beehiiv(api_key, title, content, slug=None, excerpt=None, featured_image=None):
    # Beehiiv API endpoint
    url = "https://api.beehiiv.com/v2/publications/default/posts"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare the post data
    post_data = {
        "title": title,
        "content": content,
        "status": "draft"  # You can change this to "published" if you want to publish immediately
    }

    # Add optional fields if provided
    if slug:
        post_data["slug"] = slug
    if excerpt:
        post_data["excerpt"] = excerpt
    if featured_image:
        post_data["featured_image"] = featured_image

    # Convert the data to JSON
    payload = json.dumps(post_data)

    # Make the API request
    response = requests.post(url, headers=headers, data=payload)

    # Check the response
    if response.status_code == 201:
        print("Post uploaded successfully!")
        return response.json()
    else:
        print(f"Error uploading post. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None


# Usage example
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual Beehiiv API key
    title = "My First Beehiiv Post"
    content = "<p>This is the content of my first Beehiiv post.</p>"
    
    # Optional parameters
    slug = "my-first-beehiiv-post"
    excerpt = "A short excerpt of the post content."
    featured_image = "https://example.com/image.jpg"

    result = upload_post_to_beehiiv(api_key, title, content, slug, excerpt, featured_image)
    
    if result:
        print(f"Post ID: {result['data']['id']}")
        print(f"Post URL: {result['data']['url']}")

'''

This script does the following:

1. It imports the necessary libraries: `requests` for making HTTP requests and `json` for handling JSON data.

2. It defines a function `upload_post_to_beehiiv` that takes the API key and post details as parameters.

3. The function sets up the API endpoint URL and headers, including the authorization token.

4. It prepares the post data, including optional fields if provided.

5. The function makes a POST request to the Beehiiv API with the post data.

6. It checks the response and prints a success message or error details accordingly.

7. In the usage example, it demonstrates how to call the function with sample data.

To use this script:

1. Install the `requests` library if you haven't already: `pip install requests`
2. Replace `'YOUR_API_KEY'` with your actual Beehiiv API key.
3. Modify the post details (title, content, etc.) as needed.
4. Run the script.

The script will upload the post as a draft by default. 

If you want to publish it immediately, change `"status": "draft"` to `"status": "published"` in the `post_data` dictionary.

Remember to handle your API key securely and not to share it in public repositories or unprotected environments.

'''
