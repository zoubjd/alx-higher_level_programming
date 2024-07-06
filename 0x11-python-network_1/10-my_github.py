#!/usr/bin/python3
"""takes your GitHub credentials and prints id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    passwd = argv[2]
    headers = {'Authorization': 'token {}'.format(passwd)}
    r = requests.get(url, headers=headers)
    print(r.json().get('id'))
