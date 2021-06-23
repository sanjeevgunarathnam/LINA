import os
import sys
import json


config_json_file_name: str = 'config.json'

test_config_field: str


def get_application_path() -> str:
    if getattr(sys, 'frozen', False):
        # This means application is being run as executable, so get the executable's path
        return os.path.dirname(sys.executable)
    else:
        # This means application is being run from code, so just get this module's path
        return os.path.dirname(os.path.abspath(__file__))


def init():
    global test_config_field
    config_json_file_path = os.path.join(get_application_path(), config_json_file_name)
    with open(config_json_file_path, 'r+') as config_json_file:
        config = json.load(config_json_file)
        test_config_field = config['testConfigField']
