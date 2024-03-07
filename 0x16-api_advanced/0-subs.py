#!/usr/bin/python3
"""parsing web data from an api"""
import json
import requests
import sys

def number_of_subscribers(subreddit):
    """get num of subs"""
    base_url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'Agent-Ano'}
    url = base_url + '{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    if data["kind"] != "t5":
        return 0
    return data["data"]["subscribers"]
