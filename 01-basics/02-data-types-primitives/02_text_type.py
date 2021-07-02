# string = array of char

string_value = "python is amazing"
string_value2 = 'python is amazing'
print(string_value)
print(string_value2)

# casting (convert into other type)
print("casting str")
a = str(3)
b = str(3.1416)
c = str("3.1416")
print(a)
print(b)
print(c)
print(type(c))

# one line assignment
print("one line assignment")
name_one,name_two, name_three = "rosanna","jack","bill"
print(name_one,name_two,name_three)

# one line assignment mixed types
print("one line assignment mixed types")
s,t,u = 1,"python",99
print(s,t,u)
print("type",type(s),type(t),type(u))

# concat
search_engine1 = "http://www.google.com"
search_engine2 = "http://www.duckduckgo.com"
print("concat using + ",search_engine1 + " " + search_engine2)

# concat number with string
a_number = 999
#print(a_number + search_engine2)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(a_number) + search_engine2)

# concat string with number
#print(search_engine2 + a_number)
#TypeError: can only concatenate str (not "int") to str
print(search_engine2 + str(a_number))

a_string = "Hello World!"
print(a_string)
# first element str
print("char 0","\t",a_string[0])

# slicing -> substring
print("slicing char 2 -> 4","\t",a_string[2:5])

# slicing -> substring to end
print("slicing char 2 -> end","\t",a_string[2:])

# slicing -> substring from start
print("slicing from start -> char 4","\t",a_string[:5])

# slicing -> substring negative index
print("slicing -5 -> -2 ","\t",a_string[-5:-2])

# repeat
print("str * 5","\t",a_string * 5)

# string immutable
print("immutable","\t",a_string)

# to change string -> overwrite
print("overwrite (before)","\t",a_string)
a_string = a_string * 2
print("overwrite (after)","\t",a_string)


# replace item not supported
#a_string[0] = "A"
# TypeError: 'str' object does not support item assignment

print("looping")
a_string="Hello World!"
print(a_string)
for character in a_string:
    print(character)

# length
print("length (#chars)","\t",len(a_string))

# substr in str
print("substr in")
if "ello" in a_string:
    print("ello found")

# shorter
print("ello" in a_string)
# True

# substr not in str
print("substr not in")
print("Yello" not in a_string)
# True

# if
print("if substr in")
if "Yello" or "yello" not in a_string:
    print("Yello or yello not found")

# upper
print("upper","\t",a_string.upper())
# print(upper(a_string))  # wrong !!! use . notation (=class method)

# lower
print("lower","\t",a_string.lower())
print("string immutable","\t",a_string)

# remove whitespace (trim)
a_string2 = "    Hello World!     "
print(a_string2)
print("len",len(a_string2))
print(a_string2.strip())
print("len",len(a_string2))
print(a_string2)
a_string2=a_string2.strip()
print(a_string2)
print("len",len(a_string2))

# replace string
print("replace string")
print(a_string.replace("Hello","Goodbye"))
print(a_string)

# split string ; string -> list
print("split")
a_string3 = "Array, List, Tuple, Set"
list1 = a_string3.split(",")
print(a_string3.split(","))
# ['Array', ' List', ' Tuple', ' Set']
print(type(a_string3))
print(type(list1))
a_string4 = "0 1 2 3 4 5 6 7 8 9"
print(a_string4.split(" "))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# string format
print("format using format")
name = "Joe"
age = 36
city = "New York"
txt = "My name is {}, my age is {} and I live in {}."
print(txt.format(name,age,city))
txt2 = "I live in {2}, my age is {1} and my name is {0}."
print(txt2.format(name,age,city))

# string format -> most used
print("format using f")
print(f"I live in {city}, my age is {age} and my name is {name}")

# escape chars
print("escape chars")
print("\"Python\" is cool")
print("Newline\n")

# join tuple into str
print("tuple join into str")
a_tuple = ("Alpha","Beta","Gamma")
x = "#".join(a_tuple)
print(x)
# Alpha#Beta#Gamma




















