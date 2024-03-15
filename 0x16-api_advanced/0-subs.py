#!/usr/bin/python3
"""parsing data from api"""
import json
import requests

def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com/r/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    url = base_url + '{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    try:
        resp_data = response.json()
        subscribers = resp_data['data']['subscribers']
    except (KeyError, json.JSONDecodeError):
        return 0
    
    return subscribers
