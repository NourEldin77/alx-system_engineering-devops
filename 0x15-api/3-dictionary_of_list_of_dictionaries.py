#!/usr/bin/python3
""" A script to fetch tasks data for multiple users from JSONPlaceholder API
and save it to a JSON file. """


import json
import sys
import urllib.parse
import urllib.request


def get_user(ID):
    """
    Fetch user data from the JSONPlaceholder API based on the provided user ID.

    Args:
        ID (int): The ID of the user whose data is to be fetched.

    Returns:
        dict: A dictionary containing user data.
    """
    users_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    with urllib.request.urlopen(users_url) as response:
        return json.loads(response.read().decode())


def get_tasks(ID):
    """
    Fetch tasks data from the JSONPlaceholder API based on the provided user ID

    Args:
        ID (int): The ID of the user whose tasks are to be fetched.

    Returns:
        list: A list containing task data.
    """
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    with urllib.request.urlopen(todos_url) as response:
        tasks_array = json.loads(response.read().decode())
    return tasks_array


def format_data(ID):
    """
    Format the tasks data for a specific user.

    Args:
        ID (int): The ID of the user whose tasks data is to be formatted.

    Returns:
        list: A list of dictionaries containing formatted task data.
    """
    username = get_user(ID).get("username")
    todos_data_arr = get_tasks(ID)
    formatted_data = []
    for ele in todos_data_arr:
        formatted_data.append(
            {
                "task": ele.get('title'),
                "completed": ele.get("completed"),
                "username": username
            }
        )
    return formatted_data


def create_json(filename):
    """
    Create a JSON file containing tasks data for multiple users.

    Args:
        filename (str): The name of the JSON file to be created.
    """
    tasks_dict = {}
    for i in range(1, 11):
        tasks_dict[f"{i}"] = format_data(i)

    with open(filename, 'w') as file:
        file.write(json.dumps(tasks_dict))


if __name__ == '__main__':
    filename = "todo_all_employees.json"
    create_json(filename)
