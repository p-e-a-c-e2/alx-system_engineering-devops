#!/usr/bin/python3
"""
import the modules
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    function that queries the Reddit API and returns a
    list containing    the titles of all hot articles for a given subreddit.
    """

    context = {'show': 'all'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    headers = {'User-Agent': 'Google Chrome Version 112.0.5615.49'}
    url = 'https://www.reddit.com/r/{}hot/.json?after={}'
    .format(subreddit, after)
    response = requests.get(url, headers=headers, context=context}

    if (response.status_code != 200):
        return None
    all_data = response.json()
    try:
        raw_data = all_data.get('data').get('children')
        after = all_data.get('data').get('after')

        if after is None:
            return hot_list

        for i in raw_data:
            hot_list.append(i.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    except BaseError:
        print('None')
