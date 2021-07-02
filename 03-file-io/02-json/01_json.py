import json

j1 = '{"name":"Billy Joel","city":"New York","age":55}'

# convert json -> python (load)
x1 = json.loads(j1)
print("json -> python using loads")
print("x = ",x1)
print("type = ",type(x1))   #<class 'dict'>

# convert python -> json (dump)
dict1 = {
    "name":"Billy Joel",
    "city":"New York",
    "age":33,
    "gender":"M"
}
j2 = json.dumps(dict1)
print("python -> json using dumps")
print("j = ",j2)
print("type = ",type(j2))

print("indentation")
j3 = json.dumps(dict1,indent=4)
print("j = ",j3)

print("separators")
j4 = json.dumps(dict1,indent=4,separators=(". "," = "))
print("j = ",j4)

print("sort")
j5 = json.dumps(dict1,indent=4,sort_keys=True)
print("j = ",j5)

