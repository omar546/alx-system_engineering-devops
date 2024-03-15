#!/usr/bin/python3
"""Gets subscriber count for subreddit."""
import requests


def number_of_subscribers(subreddit):
	headers = {'User-Agent': 'Ano/1.0'}
	url = f"https://www.reddit.com/r/{subreddit}/about.json"

	response = requests.get(url, headers=headers, allow_redirects=False)
	if response.status_code != 200:
		return 0

	data = response.json()
	if data["kind"] != "t5":
		return 0
	return data["data"]["subscribers"]
