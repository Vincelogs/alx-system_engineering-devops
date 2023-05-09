#!/usr/bin/python3
'''prints titles of first 10 hot posts listed for a given subreddit'''
from requests import get


def top_ten(subreddit):
    '''
    Description:
        - queries Reddit API to print first 10 host posts
    Output:
        - Success: prints first 10 host posts listed
          for a given subreddit
        - Failure: print None
    '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My User-Agent 1.0"}
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    top_10 = response.json()["data"]["children"]
    for post in top_10:
        print(post["data"]["title"])
