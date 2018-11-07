from __future__ import print_function

import json
result = {}

with open("E:\Python project\log.txt", "rb") as fd:
    country = None
    for line in fd:
        line = line.strip()
        if line == "":
            continue

        if ':' in line:
            country = line[:-1]

        else:
            city_parts = line.split(None, 1)
            result.setdefault(country, {})[city_parts[0]] = city_parts[1]

print(json.dumps(result, indent = 4).decode("unicode-escape"))





#string型转int型  
x = [ int( x ) for x in x if x ]  
y = [ int( y ) for y in y if y ]  
z = [ int( z ) for z in z if z ]  