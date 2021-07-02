f = open("text.txt", "a")
print("append line to file")
f.write("Here you read line11")
f.close()
f = open("text.txt", "r")
print(f.read())
f.close()

