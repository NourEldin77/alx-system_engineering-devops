#!/usr/bin/python3
""" ToDo: Doc """


import requests


def sort_count(item):
    """
    Helper function to sort by count in descending order
    and word in ascending order
    """
    return (-item[1], item[0])


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    ToDo: Doc
    """
    if word_counts is None:
        word_counts = {}

    if not subreddit or not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        title = post["data"].get("title", "").lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                if word_lower in word_counts:
                    word_counts[word_lower] += title.count(word_lower)
                else:
                    word_counts[word_lower] = title.count(word_lower)

    next_page = data["data"].get("after")
    if next_page:
        count_words(subreddit, word_list, next_page, word_counts)
    else:
        sorted_word_counts = sorted(word_counts.items(), key=sort_count)
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")
