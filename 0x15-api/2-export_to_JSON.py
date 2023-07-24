#!/usr/bin/python3
""" get files"""

import json
import requests
import sys


""" request to specified api url to retrieve json data """


def get_data(api_url):
    try:
        res = requests.get(api_url)

        """ raise exception errors """
        res.raise_for_status()

        """ json formatting """
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"An Error Occured: {e}")
        return None


def main():
    employee_id = sys.argv[1]

    """replacing url param with API endpoint """
    user_api_url = (
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    )
    user_data = get_data(user_api_url)

    """ user todo data """
    user_todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)
        )
    user_todos = get_data(user_todos_url)

    """ condition if user data is available """
    if user_data:
        user_id = str(user_data.get('id'))
        user_name = user_data.get('username')

        todo_list = []

        for todo in user_todos:
            new_todo = {"task": todo.get('title'),
                        "completed": todo.get('completed'),
                        "username": user_name
                        }
            todo_list.append(new_todo)

        user_json = {user_id: todo_list}
        print(user_json)

        """ write into a json file """
        if user_json:
            json_data = json.dumps(user_json)
            file_name = f"{user_id}.json"
            with open(file_name, "w") as file:
                file.write(json_data)

    else:
        print("Failed to get data")


if __name__ == "__main__":
    main()
