import requests
import random
from collections import defaultdict

# List of proxy servers from https://free-proxy-list.net/
proxy_list = [
    'https://103.237.144.232:1311',
    'https://47.88.85.102:3389',
    'https://116.203.139.209:5153',
    'http://18.135.62.35:80'
]

MAX_REQUESTS_PER_PROXY = 10
total_requests = 50
url = 'https://api.spacexdata.com/v4/launches/latest'

# Track requests per proxy
request_counter = defaultdict(int)

def get_random_proxy():
    """Select a random proxy ensuring it hasn't reached its request limit."""
    available_proxies = [proxy for proxy in proxy_list if request_counter[proxy] < MAX_REQUESTS_PER_PROXY]
    if not available_proxies:
        raise Exception("All proxies have reached their request limit.")
    return random.choice(available_proxies)

def make_requests():
    """Send requests with proxy rotation and error handling."""
    for _ in range(total_requests):
        proxy = get_random_proxy()
        request_counter[proxy] += 1
        
        proxies = {
            'http': proxy,
            'https': proxy,
        }

        try:
            response = requests.get(url, proxies=proxies, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"Request successful with proxy {proxy}: {data}")
            else:
                print(f"Request failed with proxy {proxy}, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error with proxy {proxy}: {e}")

make_requests()
