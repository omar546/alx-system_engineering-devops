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
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    try:
        data = resp.get('data')
        subscribers = data.get('subscribers')
    except:
        return 0
    if subscribers is None:
        return 0
    return int(subscribers)
