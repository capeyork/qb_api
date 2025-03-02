#!/usr/bin/env python

import json
import requests

# Load config and token
with open("config.json") as f:
    config = json.load(f)

with open("token.json") as f:
    token_data = json.load(f)

# Set up API request
realm_id = config["realm_id"]
api_url = f"{config['API_URL']}/{realm_id}/companyinfo/{realm_id}"
headers = {
    "Authorization": f"Bearer {token_data['access_token']}",
    "Accept": "application/json"
}

# Make request
response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

