#!/usr/bin/python3
"""
A script to export data in the CSV format..
"""
if __name__ == '__main__':
    import requests
    import sys
    import json

    base_url = "https://jsonplaceholder.typicode.com"

    employee_id = int(sys.argv[1])

    user_info_url = "{}/users/{}".format(base_url, employee_id)
    response = requests.get(user_info_url)
    employee_info = response.json()
    employee_name = employee_info["username"]

    todo_list_url = "{}/todos?userId={}".format(base_url, employee_id)
    response = requests.get(todo_list_url)
    todo_list = response.json()

    json_data = {}
    json_data[employee_id] = []
    for task in todo_list:
        json_data[employee_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
            })
    with open("{}.json".format(employee_id), "w") as filejson:
        json.dump(json_data, filejson)
