from curl_cffi import requests

url = 'https://duncanlutz.dev/example/%2f%2f%2f'

session = requests.Session()
response = session.get(url)

# Asserts currently fail
assert response.url == url
