#!/usr/bin/python3
"""
This script retrieves user data and associated tasks from JSONPlaceholderAPI
and saves it to CSV file It takes a user ID as input and generates a CSV file
named `USER_ID.csv` containing the user's tasks.
"""


import csv
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
        list: List of lists representing formatted data.
    """
    username = get_user(ID).get("username")
    todos_data_arr = get_tasks(ID)
    formated_Data = []
    for ele in todos_data_arr:
        formated_Data.append(
            [ID, username, ele.get("completed"), ele.get("title")])
    return formated_Data


def create_csv(filename, data_Arr):
    """
    Creates a CSV file with the provided filename and writes
    the formatted data array to it.

    Args:
        filename (str): The name of the CSV file to be created.
        data_Arr (list): List of lists representing formatted data.
    """
    with open(filename, 'w', newline='') as file:
        csv_writer_obj = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_writer_obj.writerows(data_Arr)


if __name__ == '__main__':
    # input user_ID
    user_id = sys.argv[1]
    # file_name USER_ID.csv
    filename = f"{user_id}.csv"

    create_csv(filename, format_Data(user_id))
