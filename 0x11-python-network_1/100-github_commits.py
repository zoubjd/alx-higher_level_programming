#!/usr/bin/python3
"""list 10 commits"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    if len(commits) < 10:
        for i in len(commits):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author))
    else:
        for i in range(10):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author))
