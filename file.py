import requests

def http_request_analyzer(url):
    response = requests.get(url)
    print(f"HTTP Status Code: {response.status_code}")
    print(f"HTTP Headers: {response.headers}")

url = "https://shieldinelix.com"
http_request_analyzer(url)