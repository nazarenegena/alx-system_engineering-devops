#!/usr/bin/python3
# script that returns info about employees TODO list progress

import sys
import requests

""" request to specified api url to retrieve json data """

def get_data(api_url):
    try:
        res = requests.get(api_url)

        """raise exception errors"""

        res.raise_for_status()

        """json formatting"""

        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"An Error Occured: {e}")
        return None
    
def main():
    employee_id = sys.argv[1]

    """replacing url param with API endpoint"""

    """ user data """
    user_api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    user_data = get_data(user_api_url)

    """ user todo data """
    user_todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    user_todos = get_data(user_todos_url)
    
    # user completed todo data
    completed_user_todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}&completed=true'.format(employee_id)
    completed_todos = get_data(completed_user_todos_url)

  
    """ condition if user data is available """
    if user_data:
        number_completed_todos=str(len(completed_todos))
        number_total_todos = str(len(user_todos))
        print("Employee " + user_data['name'] + " is done with tasks ("
                + number_completed_todos +"/"+ number_total_todos +"):")
        for todo in completed_todos:
            print("\t " + todo.get('title'))
    else:
        print("Failed to get data")
    
    

if __name__ == "__main__":
    main()




