#!/usr/bin/python3
"""
script to export data in the JSON format.
"""
if __name__ == "__main__":
    import json
    import requests

    base_url = "https://jsonplaceholder.typicode.com"

    response = requests.get("{}/users".format(base_url))
    employees = response.json()

    all_tasks = {}

    for employee in employees:
        employee_id = employee["id"]
        employee_name = employee["username"]

        response = requests.get("{}/todos?userId={}".format(
            base_url, employee_id))
        todo_list = response.json()

        employee_tasks = []

        for task in todo_list:
            employee_tasks.append({
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
                })
        all_tasks[employee_id] = employee_tasks
    with open("todo_all_employees.json", "w") as filejson:
        json.dump(all_tasks, filejson)
