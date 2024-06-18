#!/usr/bin/python3


""" ToDo: Doc """


import json
import urllib.request
import urllib.error


def number_of_subscribers(subreddit):
    """ ToDo: Doc """
    subreddit_url = f"https://api.reddit.com/subreddits/search?q={subreddit}"
    headers = {'User-Agent': "Custom"}
    req = urllib.request.Request(subreddit_url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        all_subreddits = data.get("data").get("children")
        first_res = all_subreddits[0].get("data")
        if first_res.get("display_name") != subreddit:
            return 0
        return (first_res.get("subscribers"))
    except urllib.error.HTTPError as e:
        return 0
    except urllib.error.URLError as e:
        return 0
