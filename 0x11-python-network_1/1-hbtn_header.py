#!/usr/bin/python3
"""sends a request to the URL and displays the value"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        html = response.read()
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
