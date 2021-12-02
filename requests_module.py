import requests

for url in ['https://api.github.com']: #, 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        #print(response.content)
        #print(response.text)
        print(response.status_code)
        response.raise_for_status()

    # except HTTPError as http_err:
    #     print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


# Parse Json
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(repository)
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}') 



rs = requests.get( 'https://api.github.com/search/repositories', params=b'q=requests+language:python')
print(rs)


 # requests.post('https://httpbin.org/post', data={'key':'value'})
 # requests.put('https://httpbin.org/put', data={'key':'value'})
 # requests.delete('https://httpbin.org/delete')
 # requests.head('https://httpbin.org/get')
 # requests.patch('https://httpbin.org/patch', data={'key':'value'})
 # requests.options('https://httpbin.org/get')

# Transport Adapters let you define a set of configurations per service you’re interacting with. 
# For example, let’s say you want all requests to https://api.github.com to retry three times before finally raising a ConnectionError. 
# You would build a Transport Adapter, set its max_retries parameter, and mount it to an existing Session:


from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)