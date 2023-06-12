#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subsrcibers
for a given subreddit
"""
def number_of_subscribers(subreddit):
    """Returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = 'mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
    agent += ' Gecko/20100101 Firefox/47.0'
    headers = {"user-Agent": agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    return 0 if response.status_code != 200 else response.json()\
            .get('data')\
            .get('subscribers')
