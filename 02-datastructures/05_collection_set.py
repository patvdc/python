# set {} : collection data type
# ordered & unindexed, unmutable (add/remove possible, update not possible), no duplicate elements

# create empty set
empty_set1 = {''}

# create empty set using constructor
empty_set2 = set()

print(empty_set1)
print(type(empty_set1))
print(empty_set2)
print(type(empty_set2))

# add item(s) to set
print("add item(s) using add")
a_set = set()
print(a_set)
a_set.add(1)
a_set.add(2)
a_set.add(3)
a_set.add(1)   #duplicate
print(a_set)
print(f"set has {len(a_set)} item(s)")

# create set with elements  using constructor
set4 = set((1,2,3,4,"apple"))
print(set4)

set1 = {"yellow","blue","orange","white"}
print(set1)
set2 = {True,False,False,False}
print(set2," ",len(set2))
set3 = {"true",True,13,"weather",20.0}
print(set3)

print("# elements")
print(len(set1))

print("access elements")
for x in set3:
    print(x)

print("set contains element")
print("weather" in set3)

# add items into other set
print("add items from other set using update")
print(set1)
print(set2)
set1.update(set2)
print(set1)

# add list to set - tuple & dict also possible
print("add list to set using update")
print(set1)
list1=["00","01","05"]
print(list1)
set1.update(list1)
print(set1)

# remove item from set
print("remove item from set using remove")
print(set1)
set1.remove(True)
set1.remove("05")
print(set1)

# remove item from set
# pop can not be used as elements are unordered
print("remove item from set using discard")
print(set1)
set1.discard(False)
print(set1)

# make set empty
print("make set empty")
print(set4)
set4.clear()
print(set4)

# delete set
print("delete set")
print(set4)
del set4

# loop through set
print("loop")
for x in set1:
    print(x)

# join 2 sets into 3e -  duplicates will be removed
print("join 2 sets into 3e using union")
print(set1)
print(set2)
set10 = set1.union(set2)
print(set10)
del set10

# insert set2 into set1 - duplicates will be removed
print("insert set2 into set1 using update")
print(set1)
print(set2)
set1.update(set2)
print(set1)

# intersection of 2 sets (only duplicates)
print("insection into existing set")
print(set2)
print(set3)
set2.intersection_update(set3)
print(set2)

# intersection 3e set used
print("intersection into new set")
print(set1)
print(set2)
set10 = set1.intersection(set2)
print(set10)
del set10

# keep all but not the duplicates into existing set
print("all elements except interception into existing set")
print(set1)
print(set2)
set1.symmetric_difference_update(set2)
print(set1)

# keep all but not the duplicates into new set
print("all elements except interception into new set")
print(set1)
print(set2)
set10 = set1.symmetric_difference(set2)
print(set10)
del set10

# remove duplicates from list -> cast into set
print("remove duplicates from list using set")
a_list=[2,4,1,2,7,9,5,1,8,6]
print(a_list)
print(set(a_list))
a_list=list(set(a_list))
print(a_list)



