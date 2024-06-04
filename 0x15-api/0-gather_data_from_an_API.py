#!/usr/bin/python3
"""This script retrieves information about an employee's TODO list progress.

The script takes user ID as input and fetches data from the JSONPlaceholder API
to determine the number of completed tasks for the specified user.

Usage:
    $ python3 todo_progress.py [user_id]

Arguments:
    user_id (int): The ID of user whose TODO list progress is to be retrieved.

Returns:
    None

Example:
    $ python3 todo_progress.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
         ...
"""

import json
import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    # Global variable to store the total number of tasks
    TOTAL_NUMBER_OF_TASKS = 0

    def get_user(ID):
        """Retrieve user data from the JSONPlaceholder API.

        Args:
            ID (int): The ID of the user to fetch data for.

        Returns:
            dict: User data as a dictionary object.
        """
        users_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
        with urllib.request.urlopen(users_url) as response:
            return json.loads(response.read().decode())

    def get_tasks(ID):
        """Retrieve TODO list data for a specific user from JSONPlaceholderAPI

        Args:
            ID (int): The ID of user whose TODO list data is to be retrieved

        Returns:
            list: A list of titles of completed tasks for the specified user.
        """
        global TOTAL_NUMBER_OF_TASKS
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
        completed_tasks = []
        with urllib.request.urlopen(todos_url) as response:
            tasks_array = json.loads(response.read().decode())
        for task in tasks_array:
            if task.get('completed') is True:
                completed_tasks.append(task.get('title'))
            TOTAL_NUMBER_OF_TASKS += 1
        return completed_tasks

    # Retrieve user data and completed tasks
    user_id = sys.argv[1]
    EMPLOYEE_NAME = get_user(user_id).get('name')
    DONE_TASKS = get_tasks(user_id)
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)

    # Print TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in DONE_TASKS:
        print("\t " + title)
