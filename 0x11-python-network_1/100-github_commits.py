#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""


if __name__ == '__main__':
    import requests
    import sys
    rep_name = sys.argv[1]
    own_name = sys.argv[2]
    f = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(own_name, rep_name))
    commits = f.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
