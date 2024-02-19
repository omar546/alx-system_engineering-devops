#!/usr/bin/python3
"""script for parsing web data from an api
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    base = 'https://jsonplaceholder.typicode.com/'
    try:
        employee_id = sys.argv[1]
    except:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        exit(1)

    url = base + 'users?id={}'.format(employee_id)
    response = requests.get(url)
    user = json.loads(response.text)
    name = user[0].get('name')

    url = base + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    done = 0
    tasks_done = []
    for obj in objs:
        if obj.get('completed'):
            tasks_done.append(obj)
            done += 1

    # print the output about user's task completion
    print("{} is done with tasks({}/{}):".format(name, done, len(objs)))
    # print the output title of completed tasks
    for task in tasks_done:
        print("\t {}".format(task.get('title')))
