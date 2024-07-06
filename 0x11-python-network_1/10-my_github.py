#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    pat = sys.argv[2]
    auth = HTTPBasicAuth(username, pat)
    url = 'https://api.github.com/user'
    f = requests.get(url,
                     auth=auth)
    print(f.json().get('id'))
