import requests
import os

auth_key = os.environ.get('USAJOB_AUTH_KEY')
user_agent = os.environ.get('USAJOB_USER_AGENT')

if not auth_key or not auth_key:
    raise ValueError("missing auth-key or user-agent")

headers = {
    "User-Agent": user_agent,
    "Authorization-Key": auth_key
}

params = {
    "Keyword": "software engineer"
}

url = "https://data.usajobs.gov/api/search"
response = requests.get(url, headers=headers, params=params)


print(response.json())

