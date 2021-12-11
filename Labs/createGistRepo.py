#!/usr/bin/env python3

import json
import requests
import os

# Setup - requires the same OS environment variable as before:
token = os.getenv('GITHUB_TOKEN')

# Use the API endpoint for repositories:
url = "https://api.github.com/user/repos"

# In the data payload, define the name of the repo. This is the only required field.
data = {"name": "my-new-repo"}

# Set up the two headers. One for accepting json, one for authentication using the token
headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}

# Use requests to POST the data and headers
r = requests.post(url, headers=headers, data=json.dumps(data))

## Visit this URL and you can see your new repo:
print("Your new repo has been created: ")
d = r.json()
link = d['html_url']
print(link)
