#!/usr/bin/python3
"""
A script to export data in the CSV format..
"""
if __name__ == '__main__':
    import requests
    import sys
    import csv

    base_url = "https://jsonplaceholder.typicode.com"

    employee_id = int(sys.argv[1])

    user_info_url = "{}/users/{}".format(base_url, employee_id)
    todo_list_url = user_info_url + "/todos"
    user_info_response = requests.get(user_info_url).json()
    todo_list_response = requests.get(todo_list_url).json()
    username = user_info_response.get("username")
    total_task = todo_list_response
    completed_task_titles = []
    for task in total_task:
        completed = {}
        completed["USER_ID"] = str(task.get("userId"))
        completed["USERNAME"] = str(username)
        completed["TASK_COMPLETED_STATUS"] = str(task.get("completed"))
        completed["TASK_TITLE"] = str(task.get("title"))
        completed_task_titles.append(completed)
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open("{}.csv".format(employee_id), "w") as csvfile:
        csv_file = csv.DictWriter(
                csvfile,
                fieldnames=header,
                quoting=csv.QUOTE_ALL
                )
        csv_file.writerows(completed_task_titles)
