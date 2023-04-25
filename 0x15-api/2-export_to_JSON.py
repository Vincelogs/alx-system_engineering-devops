#!/usr/bin/python3
''' export data in the CSV format '''
from sys import argv
from requests import get
import json


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usr = get(url + '/users/' + argv[1]).json()['username']
    todos = get(url + '/todos?userId=' + argv[1]).json()

    record, user_data, group = {}, {}, []
    for todo in todos:
        record['task'] = todo['title']
        record['completed'] = todo['completed']
        record['username'] = usr
        group.append(record)
        record = {}

    user_data[argv[1]] = group

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(user_data, file)
