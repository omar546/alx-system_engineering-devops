#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            {
                us.get("id"): [
                    {
                        "task": tod.get("title"),
                        "completed": tod.get("completed"),
                        "username": us.get("username"),
                    }
                    for tod in requests.get(url + "todos", params={"userId": us.get("id")}).json()
                ]
                for us in users
            },
            jsonfile,
        )
