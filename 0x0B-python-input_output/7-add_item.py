#!/usr/bin/python3
'''add item'''


import json
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

new_file = "add_item.json"

filename = "add_item.json"

if os.path.exists('./add_item.json'):
    ls = load_from_json_file(filename)
else:
    ls = []
for i in sys.argv[1:]:
    ls.append(str(i))
save_to_json_file(ls, filename)
