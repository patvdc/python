# returns always string so type conversion needed for numbers

print("what is your age ?")
age = input()
print("Your age = ", age)
print(type(age))

name = input("what is your name\n")   #escape newline
print("Your name = ", name)
print(type(name))

first_number = int(input('Type the first number: '))
second_number = int(input('Type the second number: '))
print("The sum is: ", first_number + second_number)