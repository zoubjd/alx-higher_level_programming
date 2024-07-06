#!/usr/bin/python3
"""list 10 commits"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/\
    commits?per_page=10'.format(argv[2], argv[1])

    r = requests.get(url)
    commits = r.json()

    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
