#!/usr/bin/python3
'''queries and returns corresponding result from the Reddit API'''
import requests


def number_of_subscribers(subreddit):
    '''
    Description:
    - queries and returns the number of subscibers
      (not active users, total subscribers) for a given subreddit.
    - returns 0 if an invalid subreddit is given
    '''
    # Set a custom user agent to avoid Too Many Requests error
    headers = {'User-Agent': 'My User-Agent 0.1'}
    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        return data['subscribers']
    else:
        return 0
