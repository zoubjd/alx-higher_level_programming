#!/usr/bin/python3
"""sends a post request and displays the value"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(url, data) as response:
        respdata = response.read()
        respdata = respdata.decode('utf-8')
        print(respdata)
