#!/usr/bin/python3
""" querie sthe Reddit API and prints titles of
the first 10 hot posts for a given subreddit """


def top_ten(subreddit):
    """querries the Reddit API and prints the
    titles of the first 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = request.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            children = data.get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print('None')
    except request.exceptions.RequestException:
        print('None')
