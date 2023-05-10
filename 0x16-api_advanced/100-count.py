#!/usr/bin/python3
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    '''Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        found_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    '''
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    children = data['data']['children']
    for child in children:
        hot_list.append(child['data']['title'])
    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, hot_list, after, counts)
    else:
        for title in hot_list:
            title_words = set(title.lower().split())
            for word in word_list:
                if word.lower() in title_words:
                    if word.lower() in counts:
                        counts[word.lower()] += title.lower().split().count(word.lower())
                    else:
                        counts[word.lower()] = title.lower().split().count(word.lower())
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print('{}: {}'.format(count[0], count[1]))
