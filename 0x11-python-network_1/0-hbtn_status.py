#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()

print('Body response:')
print('\t- type:', type(the_page))
print('\t- content:', the_page)
print('\t- utf8 content:', the_page.decode('utf8'))
