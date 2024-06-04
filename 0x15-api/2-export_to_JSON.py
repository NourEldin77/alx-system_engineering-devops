#!/usr/bin/python3

"""
This script retrieves user data and associated tasks from JSONPlaceholderAPI
and saves it to CSV file. It takes a user ID as input and generates a CSV file
named `USER_ID.csv` containing the user's tasks.
"""

import json
import sys
import urllib.parse
import urllib.request


def get_user(ID):
    """
    Retrieves user data from the JSONPlaceholder API based on provided user_ID

    Args:
        ID (int): The ID of the user to retrieve.

    Returns:
        dict: User data as a dictionary.
    """
    users_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    with urllib.request.urlopen(users_url) as response:
        return json.loads(response.read().decode())


def get_tasks(ID):
    """
    Retrieves tasks associated with the user
    from the JSONPlaceholder API based on the provided user ID.

    Args:
        ID (int): The ID of the user whose tasks are to be retrieved.

    Returns:
        list: List of task dictionaries.
    """
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    with urllib.request.urlopen(todos_url) as response:
        tasks_array = json.loads(response.read().decode())
    return tasks_array


def format_Data(ID):
    """
    Formats the retrieved user data and tasks into a list of lists,
    where each sublist represents a row in the CSV file.

    Args:
        ID (int): The ID of the user whose data is to be formatted.

    Returns:
        list: List of dicts representing formatted data.
    """
    username = get_user(ID).get("username")
    todos_data_arr = get_tasks(ID)
    formated_Data = []
    for ele in todos_data_arr:
        formated_Data.append(
            {"task": ele.get('title'),
             "completed": ele.get("completed"), "username": username})
    return formated_Data


def create_json(filename, data_Arr, USER_ID):
    """
    Creates a JSON file containing the formatted data.

    Args:
        filename (str): The name of the JSON file to be created.
        data_Arr (list): List of dictionaries representing formatted data.
        USER_ID (int): The ID of the user.

    Returns:
        None
    """
    tasks_dict = {f"{USER_ID}": data_Arr}
    with open(filename, 'w') as file:
        file.write(json.dumps(tasks_dict))


if __name__ == '__main__':
    # input user_ID
    user_id = sys.argv[1]
    # file_name USER_ID.json
    filename = f"{user_id}.json"

    create_json(filename, format_Data(user_id), user_id)
