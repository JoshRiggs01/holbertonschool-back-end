#!/usr/bin/python3
import requests
"""def get_employee employee id defines python fuctino that take one
parameter called employee id. this is help us fetch and display the todo list"""
def get_employee_todo_list_progress(employee_id):
    """https jasonplaceholder - this is where the base url of the restapi we are going to use
    in this script i am using the JASONPlaceholder API to provide dummy data for testing"""
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    """employee and todo url create a url to fetch info about the employee by using an f string to insert employee
    id into the url"""


    try:
        """in the next two lines i used requests.get to get the url
        specified employee and todos url- the response will be returned
        and stored in the _response variable"""
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        """.raise for status is a method that we can import fro the requests librart
        . it checks the status code and returns error if indicated or indicates
        success- if success no expection will be raised"""
        employee_response.raise_for_status()
        todos_response.raise_for_status()

        """in the next two lines i used the .json method of the responses
        from above to parse the data and return it as a python library"""
        employee_data = employee_response.json()
        todos_data = todos_response.json()


        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo['completed'])
        todo_titles = [todo['title'] for todo in todos_data if todo['completed']]


        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for title in todo_titles:
            print(f"\t{title}")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)


if __name__ == '__main__':
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_list_progress(employee_id)