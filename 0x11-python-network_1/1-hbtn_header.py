#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as page:
        print(page.getheader("X-Request-Id"))
