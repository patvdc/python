# dict {} : collection data type
# mutable, ordered (indexing), key:value pairs, key unique - duplicates allowed for valua

# create empty dict
empty_dict1 = {}

# create empty dict using constructor
empty_dict2 = dict()

print(empty_dict1, " -> ", type(empty_dict1))
print(empty_dict2, " -> ", type(empty_dict2))

mixed_dict = {
    "firstname": "John",
    "lastname": "Wayne",
    "age": 99,
    "films": ["film1", "film2", "film3"],
}
print(mixed_dict)
print("lastname index ->", mixed_dict["lastname"])
print("firstname get ->", mixed_dict.get("firstname"))
print(f"# elements =  {len(mixed_dict)}")

# keylist
print("keylist ->", mixed_dict.keys())
# valuelist
print("valuelist ->", mixed_dict.values())

# get keys into var
x = mixed_dict.keys()
print("get keys into var -> ", x)
# get values into var
x = mixed_dict.values()
print("get values into var -> ", x)
# get items into var
x = mixed_dict.items()
print("get items into var -> ", x)

# does key exists
if "lastname" in mixed_dict:
    print("Yes, 'lastname' is one of the keys")

# loop keynames + values
print("loop key names + values index")
for x in mixed_dict:
    print(x, "\t", mixed_dict[x])

# loop items
print("loop items")
for x, y in mixed_dict.items():
    print(x, y)

# loop keys
print("loop key")
for x in mixed_dict.keys():
    print(x)

# loop values
print("loop key values")
for x in mixed_dict.values():
    print(x)

# add key,value
mixed_dict["spousse"] = "Sofia Loren"
print("add key value ", mixed_dict)

# change value
mixed_dict["age"] = 98
print("change value using key ", mixed_dict)

# update dict
mixed_dict.update({"age": 90})
print("change value using update ", mixed_dict)

# remove item = key + value
mixed_dict.pop("spousse")
print("remove item using pop ", mixed_dict)

# remove last inserted item
mixed_dict.popitem()
print("remove last inserted item using popitem ", mixed_dict)

# remove item using del
del mixed_dict["firstname"]
print("remove using del ", mixed_dict)

# delete dict completely (garbage collection)
print("delete dict")
del empty_dict1

# copy
print("copy dict")
copy_dict = mixed_dict.copy()
copy_dict2 = dict(mixed_dict)
print(copy_dict)
print(copy_dict2)

# nested dict
print("nested dict way1")
employee_tuple = {
    "employee1": {
        "name": "Bill Gates",
        "year_in": 1982
    },
    "employee2": {
        "name": "Steve Jobs",
        "year_in": 1985
    },
    "employee3": {
        "name": "Linus Torvalds",
        "year_in": 1990
    }
}
print(employee_tuple)

# nested dict
print("nested dict way2")

employee1 = {
    "name": "Bill Gates",
    "year_in": 1982
}

employee2 = {
    "name": "Steve Jobs",
    "year_in": 1985
}

employee3 = {
    "name": "Linus Torvalds",
    "year_in": 1990
}

employee_tuple = {
    "employee1": employee1,
    "employee2": employee2,
    "employee3": employee3,
}
print(employee_tuple)

# join dict into str
print("join dict into str")
a_dict = {"Name": "John", "City": "New York"}
separator = "@"
x = separator.join(a_dict.values())
print(x,"\t",type(x))

# **kwargs -> dict of arguments
print("**kwargs arbitrary keywords")
def get_fullname(**contact):
    print("fullname -> " + contact["firstname"] + " " + contact["lastname"]," ")
    print(type(contact))   #<class 'dict'>

get_fullname(firstname="John", lastname="Python")

