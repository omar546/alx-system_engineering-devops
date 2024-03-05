#!/usr/bin/python3
""" top ten from given page"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ return top ten"""
    if not subreddit:
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Ano"
    }
    params = {
        "after": after
    }
    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False).json()
    if data == {'message': 'Not Found', 'error': 404}:
        return None
    info = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after', None)
    for dic in info:
        t = dic.get('data', {}).get('title', None)
        if t:
            hot_list.append(t)
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
