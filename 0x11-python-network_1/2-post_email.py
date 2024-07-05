#!/usr/bin/python3
"""sends a post request and displays the value"""
from urllib import parse, request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}

    data = parse.urlencode(values)
    data = data.encode('utf-8')

    """with request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode('utf-8'))"""
    with request.Request(url, data) as response:
        resp = request.urlopen(response)
        respdata = resp.read().decode('utf-8')
        print(respdata)
