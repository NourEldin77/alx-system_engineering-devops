#!/usr/bin/python3
import requests
""" ToDo: Doc"""


def recurse(subreddit, hot_list=None, after=""):
    """
    ToDo : Doc
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            hot_list.append(title)

    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
