# r = read, a = append, w = write, x = create
# b = binary, t = text

#f = open("text.01-txt","rt")
f = open("text.txt")
print(f)

print("read whole file")
print(f.read())
f.close()

