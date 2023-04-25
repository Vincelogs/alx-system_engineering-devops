#!/usr/bin/python3
"""gather data from an API"""
import requests as rq
from sys import argv

if __name__ == '__main__':
    # Base URL for the JSONPlacehoder API
    url = "https://jsonplaceholder.typicode.com"

    # Get user ID as arg
    user_id = int(argv[1])

    # Send a GET request to the API to get the user's name
    user_name = rq.get(f"{url}/users/{user_id}").json()["name"]

    # Send a GET request to the API to get the user's TODO_list
    todos = rq.get(f"{url}/todos?userID={user_id}").json()

    #  Extract user specific todos
    user_todos = []
    for todo in todos:
        if todo['userId'] == user_id:
            user_todos.append(todo)

    # Calculate the number of completed and total tasks
    total_tasks = len(user_todos)
    completed_tasks = len([todo for todo in user_todos if todo["completed"]])

    # Print the information about the user's TODO list progress
    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, completed_tasks, total_tasks))
    for todo in user_todos:
        if todo["completed"]:
            print('\t {}'.format(todo['title']))
