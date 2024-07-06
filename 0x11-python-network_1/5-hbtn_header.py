#!/usr/bin/python3
"""sends a request to the URL and displays the value"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    html = response.read()
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
