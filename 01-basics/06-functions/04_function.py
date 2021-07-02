# arguments

print("2 args")
def my_function(fname,age):
    print("2 arguments")
    print(fname + " => " + str(age))

my_function("John",32)

# *args
print("*args")
def my_function2(*numbers):
  print("Last nr : " + str(numbers[2]))

my_function2("one", "two", "three")

# keywords args
print("keyword args")
def my_function3(name1,name2,name3):
    print("name3 = " + name3)

my_function3(name3="John",name2="Marie",name1="Brian")

# **kwargs -> dict of arguments
print("**kwargs arbitrary keywords")
def get_fullname(**contact):
    print("fullname -> " + contact["firstname"] + " " + contact["lastname"])

get_fullname(firstname="John",lastname="Python")

#default value
print("default value")
def get_country(country = "UK"):
    return country

print("country",get_country("FR"))
print("country",get_country())

# list, tuple, set as argument
print("list, tuple,  set as argument")
def print_sequence(seq):
    print(type(seq)," => ",seq)
    for x in seq: print(x,type(x))

a_list = ["a","list","datastructure"]
a_tuple = ("a","tuple","datastructure")
a_set = {"a","set","datastructure"}
a_dict = {1:"a",2:"set",3:"datastructure"}
print_sequence(a_list)
print_sequence(a_tuple)
print_sequence(a_set)
print_sequence(a_dict)




