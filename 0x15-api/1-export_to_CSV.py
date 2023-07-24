#!/usr/bin/python3
""" get files"""
import csv
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

    """ replacing url param with API endpoint """
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

    """ condition if user data is available  """
    if user_data:
        user_id = str(user_data.get('id'))
        user_name = user_data.get('username')

        """ counting the no of completed tasks and save in csv file """
        csv_data = []
        for todo in user_todos:
            csv_data.append([user_id, user_name, todo.get(
                'completed'), todo.get('title')])

        """save data to the csv file """
        if csv_data:
            file_name = f"{user_id}.csv"
            with open(file_name, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(csv_data)
            print(file_name)

    else:
        print("Failed to get data")


if __name__ == "__main__":
    main()
