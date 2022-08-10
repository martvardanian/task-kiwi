import json
import os
from datetime import datetime

def get_info(path):
    with open(path, 'r') as user:
        data = json.load(user)
    return data


dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = f"{dir_path}/user_info.json"


info = get_info(file_path)

now = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
new_email = now + info['users']['new_user']['email']
verified_email = info['users']['verified_user']['email']
password = info['users']['new_user']['password']

