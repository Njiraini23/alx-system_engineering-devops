#!/usr/bin/python3
"""contains recursive function"""
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            reddits = response.json()

            children = reddits.get('data').get('children')
            for title in children:
                hot_list.append(title.get('data').get('title'))
            return hot_list
        return None

    except exceptions.RequestException:
        print(None)
        return 0
