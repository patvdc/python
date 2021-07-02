# array [] : collection data type
# use list (no array datatype) or numpy -> faster
# ordered, mutable, duplicate elements allowed

computer = ["dell","apple","samsung","lenovo"]
print(computer)
print(computer[3])

print("modify")
computer[2]="hp"
print(computer)

print("len")
x = len(computer)
print(x)

print("loop")
for x in computer:
    print(x)

print("add element")
computer.append("chromebook")
print(computer)

print("remove element using index")
computer.pop(1)
print(computer)

print("remove element using value")
computer.remove("lenovo")
print(computer)













