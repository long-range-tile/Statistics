#!/usr/bin/python3

import json

DATA_FILEPATH = '' # Enter filepath here

file1 = open(DATA_FILEPATH, 'r')
Lines = file1.readlines()

# AGGREGATE

DATA = {"N/A": 0}

for line in Lines:
    data_json = json.loads(line)
    if "Manufacturer Data UUID16" in data_json:
        manufacturer = data_json["Manufacturer Data UUID16"]
    
        if manufacturer in DATA:
            DATA[manufacturer] += 1
        else:
            DATA[manufacturer] = 1
    else:
        DATA['N/A'] += 1

print(dict(sorted(DATA.items(), key=lambda item: item[1])))

other = 0
exclude = ['4c', '75', '06', 'e0', 'N/A']
for item in DATA.items():
    if str(item[0]) not in exclude:
        other += int(item[1])

print('other: ', other)