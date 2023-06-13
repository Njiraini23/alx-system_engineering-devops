#!/usr/bin/python3
"""A recursive function that querries reddit API
"""


def recurse(subreddit, hot_list=[]):
    """ Returns a list containing the titles of all
    hot articles for a given subreddit
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
