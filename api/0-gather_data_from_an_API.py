#!/usr/bin/python3
""" This script uses REST API to retrieve the task completed
    by a given employee ID """

import requests


def get_employee_todo_list_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    :param employee_id: The ID of the employee to retrieve TODO list progress.
    :type employee_id: int
    """
    # Base URL of the REST API.
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Try to fetch data from the API and handle potential exceptions.
    try:
        # Fetch employee and todos data from the specified URLs.
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        # Check the status codes for potential errors.
        employee_response.raise_for_status()
        todos_response.raise_for_status()

        # Parse the data and convert it to Python dictionaries.
        employee_data = employee_response.json()
        todos_data = todos_response.json()

        # Extract relevant information from the data.
        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data 
            if todo['completed'])
        todo_titles = [todo['title'] for todo in todos_data if todo['completed']]
        
        
        # Print the employee's TODO list progress in the specified format.
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for title in todo_titles:
            print(f"\t{title}")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == '__main__':
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_list_progress(employee_id)
