import os, json

def read_json(file_name: str):
    path = os.path.abspath(__file__ + '/../../static/' + file_name)
    with open(path, encoding = 'utf-8') as file:
        return json.load(file)
    