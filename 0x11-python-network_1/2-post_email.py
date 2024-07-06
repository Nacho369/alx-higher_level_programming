#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import sys
import urllib
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    """Data should be in bytes"""
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
