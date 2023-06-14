#!/usr/bin/python3
'''json to obj'''

def load_from_json_file(filename):
    '''json to ob'''
    with open(filename) as f:
        return json.load(f)
