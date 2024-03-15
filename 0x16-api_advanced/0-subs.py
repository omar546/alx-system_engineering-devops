#!/usr/bin/python3
"""parsing data from api"""
import json
import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers"""
    base_url = 'https://www.reddit.com/r/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    # grab info about all users
    url = base_url + '{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    try:
        # grab the info about the users' tasks
        data = resp.get('data')
        subscribers = data.get('subscribers')
    except:
        return 0
    if subscribers is None:
        return 0
    return int(subscribers)
