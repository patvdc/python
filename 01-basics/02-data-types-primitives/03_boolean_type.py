x = True
y = False

print(x,y)
print(type(x),type(y))

a = 10
b = 20
c = 0

if a > b:
    print("greater")
else:
    print("not greater")

print(bool(a),bool(c))

s = "a string"
t = ""
print(bool(s),bool(t))

l1 = list(["10","20","30"])
l2 = list(("10","20","30"))

print(type(l1),type(l2))
print(bool(l1),bool(l2))

print("all False")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))






