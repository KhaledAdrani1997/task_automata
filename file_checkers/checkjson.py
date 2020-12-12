#!/usr/bin/python
#Source: https://ostoday.org/linux/how-to-run-a-python-script-in-linux.html 
import os
import sys
import json

try:
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            file = open(sys.argv[1], "r")
            json.load(file)
            file.close()
            print("Validate JSON!")
        else:
            print(sys.argv[1] + " not found")
    else:
        print("Usage: checkjson.py <file>")
except Exception as e:
    print('Error: ',e)

#to use in terminal:  checkjson test.json