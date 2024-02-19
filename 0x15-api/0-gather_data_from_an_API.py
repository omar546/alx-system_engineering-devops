#!/usr/bin/python3
"""
returns info about employee Tasks progress using api
"""
import re
import requests
import sys

"""REST-API"""
API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(API, id)).json()
            result = requests.get('{}/todos'.format(API)).json()
            user_name = user.get('name')
            todoz = list(filter(lambda x: x.get('userId') == id, result))
            todoz_done = list(filter(lambda x: x.get('completed'), todoz))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todoz_done),
                    len(todoz)
                )
            )
            for done in todoz_done:
                print('\t {}'.format(done.get('title')))
