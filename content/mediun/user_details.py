import requests
import configparser

config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

# Replace with your actual Medium integration token and user ID
MEDIUM_TOKEN = config['medium']['access']

headers = {
    'Authorization': f'Bearer {MEDIUM_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'host': 'api.medium.com',
    'Accept-Charset': 'utf-8'
}
url = '''https://api.medium.com/v1/me'''
response = requests.get(url=url, headers=headers)

print('status_code is: ', response.status_code)
print('response text:', response.json())
print('userId:', response.json()['data']['id'])