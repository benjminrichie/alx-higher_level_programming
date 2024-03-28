#!/usr/bin/python3
"""To send POST request to a particular URL with an email.
Usage: ./6-post_email.py <URL> <email>
  - To display the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
