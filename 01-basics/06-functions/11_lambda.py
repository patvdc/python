people = [
    {"name": "John", "city": "New York"},
    {"name": "Bill", "city": "London"},
    {"name": "Francois", "city": "Paris"}
]

def f(person):
#    return person["name"]
    return person["city"]

print("using def function")
people.sort(key=f)
print(people)
# TypeError: '<' not supported between instances of 'dict' and 'dict'

print("using lambda")
# lambda -> input person -> output person["name"]
people.sort(key=lambda person: person["name"])
print(people)