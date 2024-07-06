#!/usr/bin/python3
"""searches for a user and prints it"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    payload = {'q': q}
    r = requests.post(url, data=payload)
    try:
        j = r.json()
        if j:
            print("[{}] {}".format(j['id'], j['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
