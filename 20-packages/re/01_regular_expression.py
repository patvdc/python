# search pattern

import re

string = "python comes from monty python and not from the snake"
x1 = re.search("^python",string)
if x1:
    print("starts with python")
else:
    print("no match")

x2 = re.search("^python.*snake$",string)
if x1:
    print("starts with python & ends with snake")
else:
    print("no match")