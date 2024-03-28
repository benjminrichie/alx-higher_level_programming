#!/usr/bin/python3
"""To use the GitHub API and display
GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Also use Basic Authentication to access ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
