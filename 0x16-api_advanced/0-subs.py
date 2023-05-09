#!/usr/bin/python3
"""
import the modules
"""
import requests


def number_of_subscribers(subreddit):
    """ set the custom User_agent"""
    headers = {'User-Agent': 'Google Chrome Version 112.0.5615.49'}

    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
