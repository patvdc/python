import os

print("delete file")
if os.path.exists("text2.txt"):
    os.remove("text2.txt")
else:
    print("file does not exist")
