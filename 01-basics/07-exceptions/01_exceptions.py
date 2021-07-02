import sys

try:
    x = int(input("x = "))
    y = int(input("y = "))
except ValueError:
    print("ERROR : invalid input")
    sys.exit(1)

# ValueError: invalid literal for int() with base 10: 'james'

# try to divide by 0
try:
    result = x/y
except ZeroDivisionError:
    print("ERROR : can not devide by 0.")
    sys.exit(1)

print(f"{x} divided by {y} = {result}")

# ZeroDivisionError: division by zero



