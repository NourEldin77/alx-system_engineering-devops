#!/usr/bin/python3
""" ToDo: Doc """

import requests
import json


def top_ten(subreddit):
    """ ToDo: Doc """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': "Custom"}
    params = {"limit": 10}
    request = requests.get(url, headers=headers, params=params)
    if request.status_code != 200:
        print(None)
        return
    responses = request.json()
    responses = responses["data"]["children"]
    for response in responses:
        print(response["data"]["title"])
