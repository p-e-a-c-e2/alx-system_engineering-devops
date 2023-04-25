#!/usr/bin/python3
"""
A script using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
if __name__ == '__main__':
    import requests
    import sys

    base_url = "https://jsonplaceholder.typicode.com"

    employee_id = int(sys.argv[1])

    user_info_url = "{}/users/{}".format(base_url, employee_id)
    user_info_response = requests.get(user_info_url)
    user_info = user_info_response.json()
    employee_name = user_info["name"]

    todo_list_url = "{}/todos?userId={}".format(base_url, employee_id)
    todo_list_response = requests.get(todo_list_url)
    todo_list = todo_list_response.json()

    completed_tasks = 0
    total_tasks = len(todo_list)
    completed_task_titles = []
    for task in todo_list:
        if task["completed"]:
            completed_tasks += 1
            completed_task_titles.append(task["title"])

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            completed_tasks,
            total_tasks
            )
        )
    for title in completed_task_titles:
        print("\t {}".format(title))
