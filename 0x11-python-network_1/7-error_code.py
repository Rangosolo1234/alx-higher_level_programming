#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response."""

import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":

    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print('Error code:', e.response.status_code)
