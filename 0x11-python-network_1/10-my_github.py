#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    passwd = argv[2]
    req = requests.get(url, auth=(user, passwd))
    print(req.json().get("id"))
