#!/usr/bin/python3
'''to json file'''


def save_to_json_file(my_obj, filename):
    '''to json files'''
    with open(filename, 'w') as wr:
        json.dump(my_obj, wr)
