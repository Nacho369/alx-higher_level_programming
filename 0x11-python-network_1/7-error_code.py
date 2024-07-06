#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    f = requests.get(url)
    status = f.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(f.text)
