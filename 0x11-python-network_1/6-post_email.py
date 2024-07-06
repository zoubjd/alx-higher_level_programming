#!/usr/bin/python3
"""sends a post request and displays the value"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    req = requests.post(url, email)

    print(req.text)
