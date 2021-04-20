#!/usr/bin/python3
import json

DATA_FILEPATH = '' # Enter filepath here

file1 = open(DATA_FILEPATH, 'r')
Lines = file1.readlines()

manu = 0
service = 0
both = 0
total = 0

for line in Lines:
    data_json = json.loads(line)

    if "Manufacturer Data UUID16" in data_json:
        manu += 1
    if "Service Data UUID16" in data_json:
        service += 1
        if 'feed' in data_json.values():
            print(line)
    if "Manufacturer Data UUID16" in data_json and "Service Data UUID16" in data_json:
        print(line)
        both += 1
    total += 1
    
print('manu: ', manu)
print('service: ', service)
print('both: ', both)
print('total: ', total)