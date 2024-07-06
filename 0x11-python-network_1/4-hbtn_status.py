#!/usr/bin/python3
"""Python script that fetches url using request package"""
import requests


if __name__ == '__main__':
    f = requests.get('https://alx-intranet.hbtn.io/status')
    status = f.text
    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
