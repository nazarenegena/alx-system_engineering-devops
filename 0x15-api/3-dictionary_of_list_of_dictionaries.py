#!/usr/bin/python3
""" get files"""

import json
import requests


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
    """ user todo data """
    user_todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user_todos = get_data(user_todos_url)

    todo_dict = {}

    for todo in user_todos:
        user_id = todo.get("userId")
        user = get_data(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
        new_todo = {"task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user.get('username')
                    }

        if user_id in todo_dict:
            todo_dict[user_id].append(new_todo)
        else:
            todo_dict[user_id] = [new_todo]

    print(todo_dict)

    """ write into a json file """
    if todo_dict:
        json_data = json.dumps(todo_dict)
        file_name = "todo_all_employees.json"
        with open(file_name, "w") as file:
            file.write(json_data)

    else:
        print("Failed to get data")


if __name__ == "__main__":
    main()
