#!/usr/bin/python3
""" Calling to an api and etting todos task of an specific user """
import requests
import sys

if __name__ == '__main__':
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]),
        verify=False).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            sys.argv[1]),
        verify=False).json()

    complete = [task.get('title')
                for task in todos if task.get('completed')]
    print(
        'Employee {} is done with tasks({}/{}):'.
        format(user['name'],
               complete.__len__(),
               todos.__len__()))
    print("\n".join("\t {}".format(task) for task in complete))
