#!/usr/bin/python3
"""displays header var"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rq = requests.get(url)
    print(rq.headers.get("X-Request-Id"))
