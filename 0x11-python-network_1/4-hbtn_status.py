#!/usr/bin/python3
"""Python script that fetche using request"""
import request


if __name__ == "__main__":

    resp = request.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
    print("\t- utf8 content: {}".format(resp.read().decode('utf-8')))
