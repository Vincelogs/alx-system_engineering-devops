#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """     Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code != 200:
        return None
    data = response.json()['data']
    hot_posts = data['children']
    for post in hot_posts:
        hot_list.append(post['data']['title'])
    if data['after'] is None:
        return hot_list
    return recurse(subreddit, hot_list, after=data['after'])
