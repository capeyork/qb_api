#!/usr/bin/env python

import webbrowser
import urllib.parse
import requests
import json

# Load client credentials from config.json
with open("config.json", "r") as f:
    config = json.load(f)

client_id = config["client_id"]
client_secret = config["client_secret"]
redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
scope = "com.intuit.quickbooks.accounting"
state = "random_state_string"  # Change this if needed

# Step 1: Open Authorization URL in Firefox
params = {
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": scope,
    "state": state
}
auth_url = "https://appcenter.intuit.com/connect/oauth2?" + urllib.parse.urlencode(params)

try:
    webbrowser.get("firefox").open(auth_url)
except webbrowser.Error:
    print("Firefox not found. Falling back to default browser.")
    webbrowser.open(auth_url)

# Step 2: Get Authorization Code
auth_code = input("Paste the authorization code from the redirect URL: ").strip()

# Step 3: Exchange Authorization Code for Access & Refresh Tokens
token_url = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret
}

response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    tokens = response.json()
    with open("token.json", "w") as f:
        json.dump(tokens, f, indent=2)
    print("Tokens saved to token.json.")
else:
    print("Error getting access token:", response.json())

