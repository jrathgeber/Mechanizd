import requests
import json

def post_to_linkedin(access_token, person_urn, message):
    """
    Function to post a message to LinkedIn
    
    Args:
    access_token (str): LinkedIn OAuth 2.0 access token
    person_urn (str): Your LinkedIn Person URN (Unique Resource Name)
    message (str): The content you want to post
    
    Returns:
    dict: Response from LinkedIn API
    """
    # LinkedIn API endpoint for creating a post
    url = "https://api.linkedin.com/v2/ugcPosts"
    
    # Prepare the request payload
    payload = {
        "author": f"urn:li:person:{person_urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": message
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
        }
    }
    
    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {access_token}",
        "cache-control": "no-cache",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    
    try:
        # Send POST request to LinkedIn
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Check if the post was successful
        if response.status_code == 201:
            print("Post successfully shared on LinkedIn!")
            return response.json()
        else:
            print(f"Failed to post. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Replace these with your actual values
    ACCESS_TOKEN = "your_linkedin_access_token"
    PERSON_URN = "your_linkedin_person_urn"
    MESSAGE = "Hello, this is a test post from my Python script!"
    
    # Call the posting function
    post_to_linkedin(ACCESS_TOKEN, PERSON_URN, MESSAGE)

if __name__ == "__main__":
    main()
