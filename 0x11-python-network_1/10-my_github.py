#!/usr/bin/python3
"""Python script that takes GitHub credentials (username and
password) and uses the GitHub API to display the user id."""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
