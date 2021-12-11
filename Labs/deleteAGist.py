#!/usr/bin/env python3

import json
import requests
import os

## Setup
## This snippet assumes you have a Github tokeon available as an OS
## environment variable named "GITHUB_TOKEN"

## Delete a gist

token = os.getenv('GITHUB_TOKEN')
gist_id = "b7965854c7b14ac5b8079d1bdde9e83d"

# Set up a full path with the gist_id as a path parameter:
base_url = "https://api.github.com/gists/"
url = base_url + gist_id

# Add a second header for application/json:
headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
r = requests.delete(url, headers=headers)

print("Your gist has been deleted: ")