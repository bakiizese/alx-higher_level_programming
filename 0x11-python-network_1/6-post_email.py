#!/usr/bin/python3
"""script that posts a rq"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    rq = requests.post(url, data=value)
    print(rq.text)
