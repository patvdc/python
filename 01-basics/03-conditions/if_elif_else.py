# if
print("if")
a = 20
b = 100
if a < b:
    print("a lt b")
    print("b gt a")

# if elif
print("elif")
a = 20
b = 20
if a < b:
    print("a lt b")
elif a == b:
    print("a eq b")


# if elif
print("else")
a = 19
b = 20
if a < b:
    print("a < b")
elif a == b:
    print("a == b")
else:
    print("a > b")

# ternary operator if
print("ternary if")
if a > b: print("a > b ")

# ternary operator if else
print("ternary if else")
print("a > b") if a > b else print("a =< b")

# ternary operator if elif else
print("ternary if else")
print("greater") if a > b else print("equal") if a == b else print("less")

# and
print("and")
a,b,c = 10,20,30
if c > a and c > b:
    print("true true")

# or
print("or")
a,b,c = 10,20,30
if a > b or b > c:
    print("one of conditions is true")
else:
    print("all conditions are false")

# nested if
print("nested if")
x = 100
if x > 50:
    print(">50")
    if x > 80:
        print("> 50 and > 80")
    else:
        print("> 50 and <= 80")

# avoid error
a = 10
b = 100
if b > a:
    pass

