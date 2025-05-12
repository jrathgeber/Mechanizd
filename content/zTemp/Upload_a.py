import requests

API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
BASE_URL = 'https://api.convertkit.com/v3/'

def upload_post_to_convertkit(title, content, published_at=None):
    endpoint = f'{BASE_URL}posts'
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'post': {
            'title': title,
            'content': content,
        }
    }
    
    if published_at:
        data['post']['published_at'] = published_at
    
    response = requests.post(endpoint, json=data, headers=headers)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error uploading post: {response.status_code} - {response.text}")

if __name__ == '__main__':
    title = "My New Post"
    content = "This is the content of my new post."
    
    result = upload_post_to_convertkit(title, content)
    print(f"Post uploaded successfully. Post ID: {result['post']['id']}")