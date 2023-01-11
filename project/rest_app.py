import os
import signal

from flask import Flask, request

from db_connector import add_user, get_user, update_user, delete_user


app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        if get_user(user_id) == None:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            add_user(user_id, user_name)
            return {'status id': 'ok', 'user_added': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'id already exists'}, 500  # status code

    elif request.method == 'GET':
        user_name = get_user(user_id)
        if user_name != None:
            return {'status id': 'ok', 'user_name': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'PUT':
        if get_user(user_id) != None:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            update_user(user_id, user_name)
            return {'status id': 'ok', 'user_updated': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'DELETE':
        user_name = get_user(user_id)
        if get_user(user_id) != None:

            delete_user(user_id)
            return {'status id': 'ok', 'user_deleted': user_name}, 200  # status code
        else:
            return {'status id': 'error', 'reason': 'no such id'}, 500  # status code


@app.route('/stop_server')
def stop_server():
    print('hello test gal 5000')

    # os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
