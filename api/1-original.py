#!/usr/bin/python3
""" This script uses REST API to retrieve the task completed
    by a given employee ID, then exports it to a csv file """

import requests
import csv

def get_employee_todo_list_progress(employee_id):

    """Fetches and displays the TODO list progress for a given employee ID.
    :param employee_id: The ID of the employee to retrieve TODO list progress.
    :type employee_id: int"""
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        employee_response.raise_for_status()
        todos_response.raise_for_status()

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo['completed'])
        todo_titles = [todo['title'] for
                       todo in todos_data if todo['completed']]

        # Print the employee's TODO list progress in the specified format.
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for title in todo_titles:
            print(f"\t{title}")

        # Export the data to CSV format
        file_name = f"{employee_id}.csv"
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos_data:
                user_id = todo['userId']
                username = employee_data['username']
                task_completed_status = todo['completed']
                task_title = todo['title']
                writer.writerow([user_id, username, task_completed_status, task_title])
        print(f"Data exported to {file_name} successfully.")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == '__main__':
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_list_progress(employee_id)
