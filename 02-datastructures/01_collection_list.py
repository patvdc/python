# list [] : collection data type
# ordered, mutable, duplicate elements allowed

# create empty list
empty_list1 = []
print("emptylist\t\t",empty_list1)

# create empty list using constructor method
empty_list2 = list()
print("emptylist\t\t",empty_list2)

# same data types with duplicates
string_list = ["John", "Mike", "pat","Zorba","Sandra","Kelly", "Mike","Anna","Brian"]
print("string list\t\t",string_list)

number_list = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("number list\t\t",number_list)

boolean_list = [False, False, True, False]
print("boolean list\t",boolean_list)

# different data types
mixed_list = ["Peter", "Smith", 34, True, "male"]
print("mixed list\t\t", mixed_list)

# create list using constructor, type conversion list -> string
# using ()
char_list = list(("a", "b", "c", "d", "e"))
print("char list\t\t", char_list,"\t",type(char_list))

# using []
ten_list = list([10,20,30])
print("ten list\t\t", ten_list,"\t",type(ten_list))

# get first element
item = string_list[0]
print("get first element\t", item)

# get last element
print("get last element\t\t", string_list[-1])

# get sublist - slicing - start & stop index
print("get sublist\t\t", number_list[3:9])

# get sublist from beginning - slicing
print("get sublist from beginning\t\t", number_list[:6])

# get sublist till end - slicing
print("get sublist till end\t\t", number_list[3:])

# get sublist from end - slicing
print("get sublist from end\t\t", number_list[-4:-1])

# get sublist - slicing - step index
print("get sublist step index\t\t", number_list[::2])

# class type
print("class type\t\t", type(string_list))

# nr elements in list
print("# elements in list\t\t", len(string_list))

# iterate for each
print("loop for each")
for s in string_list:
    print(s, "\t", type(s))

# loop for each range
print("loop for each range")
for i in range(len(string_list)):
    print(string_list[i],"\t",type(string_list[i]))

# loop while
print("loop while")
i = 0
while i < len(string_list):
    print(string_list[i], "\t", type(string_list[i]))
    i += 1

# loop list comprehension
print("loop list comprehension")
[print(s,"\t",type(s)) for s in string_list]

# loop
print("loop contains letter")
string_list1 = []
for s in string_list:
    if "a" in s:
        string_list1.append(s)
print(string_list1)

# check if item is list
print("item in list?")
if "Peter" in string_list:
    print("found")
else:
    print("not found")

# change item
print("change item")
print(string_list, "\t", type(string_list))
string_list[0] = "James"
print(string_list, "\t", type(string_list))

# append item
print("mixed_list append")
print("mixed list\t",mixed_list)
mixed_list.append("last item")
print("mixed list\t",mixed_list)

# insert item
print("mixed_list insert")
print("mixed list\t",mixed_list)
mixed_list.insert(2, "inserted item")
print("mixed list\t",mixed_list)

# remove first item using pop and del and index
print("remove first item using pop and del and index")
print("mixed list\t",mixed_list)
mixed_list.pop(0)
print("mixed list\t",mixed_list)
del mixed_list[0]
print("mixed list\t",mixed_list)

# remove last item using pop and index
print("remove last item using pop and index")
print("number list\t",number_list)
number_list.pop()
print("number list\t",number_list)
number_list.pop(-1)   #same
print("number list\t",number_list)

# remove item using remove and value
print("remove item using remove and value")
print("number list\t",number_list)
number_list.remove(0)
print("number list\t",number_list)

# clear list -> empty list
print("clear list")
print(boolean_list)
boolean_list.clear()
print(boolean_list)

# delete entire list
print("delete entire list")
print(boolean_list)
del boolean_list
#print(boolean_list)    #NameError: name 'boolean_list' is not defined

# reverse list -> original list changed
print("reverse list")
print(string_list)
string_list.reverse()
print(string_list)

# sort list -> original list changed
print("sort list")
print(string_list)
string_list.sort()
print(string_list)

print("sort list descending")
print(string_list)
string_list.sort(reverse=True)
print(string_list)

print("sort list descending")
print(string_list)
string_list.sort(key=str.lower)
print(string_list)

# keep original, put sorted into new list
original_list = [9,1,-3,27,3,0,-6,]
print("sort list into new list")
print(original_list)
sorted_list = sorted(original_list)
print(original_list)
print(sorted_list)

# create list with same elements
zero_list = [0] * 10
print(zero_list)

print("copy list using copy")
aaa_list = list(("a")) * 10
bbb_list = list(["b"]) * 5
print(aaa_list,"\t",len(aaa_list))
print(bbb_list,"\t",len(bbb_list))
aaa_list = bbb_list.copy()   # aaa_list replaced
print(aaa_list,"\t",len(aaa_list))
del bbb_list

print("copy list using constructor")
aaa_list = list(("a")) * 10
print(aaa_list)
destination_list = list(aaa_list)
print(destination_list,"\t",len(destination_list))
del aaa_list

# extend using concat +
print("extend with list using concat +")
aaa_list = list(("a")) * 10
bbb_list = list(["b"]) * 5
print(aaa_list)
aaa_list += bbb_list
print(aaa_list)

# extend list with other list
print("extend with list using extend method")
print(string_list)
print(char_list)
string_list.extend(char_list)
print(string_list)

# extend list with tuple
print("extend with tuple")
tuple1 = ("alpha", "beta")
print(mixed_list)
print(tuple1)
mixed_list.extend(tuple1)
print(mixed_list)

# extend with dictionary
print("extend with dict")
dict1 = {'one': 'value1', 'two': 'value2'}
print(mixed_list)
print(dict1)
mixed_list.extend(dict1)
print(mixed_list)

# replace items
print("replace items")
print(mixed_list)
mixed_list[1:2] = ["Zorro", "Tarzan"]
print(mixed_list)

# replace all items
print("replace all items")
aaa_list = list(("a")) * 10
print(aaa_list)
aaa_list[0:] = ["Ten", "Eleven"]
print(aaa_list)

print("append list2 to list1 using for and append")
list1 = ["abc"]*4
list2 = ["123"]*3
print(list1)
print(list2)
for x in list2:
    list1.append(x)
print(list1)

print("append list2 to list1 using extend")
print(list1)
print(list2)
list1.extend(list2)
print(list1)

# unpack list
colors = ["yellow","blue","green"]
a,b,c = colors
print(a)
print(b)
print(c)

print("list comprehension")
string_list1 = [s for s in string_list if "a" in s]
print(string_list1)
del string_list1

print("list comprehension condition -> removes 2 from list")
string_list1 = [i for i in number_list if i != 2]
print(string_list1)
del string_list1

print("list comprehension -> print all elements")
string_list1 = [x for x in string_list]
print(string_list1)
del string_list1

print("list comprehension -> add 0,1,2,3 .. 9")
string_list1 = [x for x in range(10)]
print(string_list1)
del string_list1

print("list comprehension condition -> add 1,2,3, .. ")
number_list1 = [x for x in range(10) if x < 5]
print(number_list1)
del number_list1

print("list comprehension -> set all elements to upper")
list10 = [x.upper() for x in string_list]
print(list10)
del list10

print("list comprehension -> set all elements to the same value")
list10 = ['test' for x in char_list]
print(list10)
del list10

print("list comprehension -> replace value")
print(string_list)
list10 = [x if x != "Mike" else "Zorro" for x in string_list]
print(list10)
del list10

print("list comprehension -> square")
num_list = [1,2,3,4,5,6]
num_list2 =[i*i for i in num_list]
print(num_list)
print(num_list2)

# from string to list -> split
a_string = "0,1,2,3,4,5,6,7,8,9"
print(a_string.split(","))

# copy list using slicing
print("copy list using slicing")
list_ori = ["one","two","three"]
list_copy = list_ori[:]
print(list_copy)





