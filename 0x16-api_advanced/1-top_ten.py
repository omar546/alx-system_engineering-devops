#!/usr/bin/python3
"""parsing web data from an api"""
import json
import requests
import sys


def top_ten(subreddit):
    '''get top ten'''
    base_url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'Agent-Ano'}
    url = base_url + '{}/top/.json?count=10'.format(subreddit)
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    try:
        data = resp.get('data')
        children = data.get('children')
    except:
        print('None')
    if children is None or data is None or len(children) < 1:
        print('None')

    for i, post_dict in enumerate(children):
        if i == 10:
            break
        print(post_dict.get('data').get('title'))
