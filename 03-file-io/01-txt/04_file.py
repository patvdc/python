f = open("text.txt", "r")
print("loop")
for line in f:
     print(line)
print("close file")
f.close()