# iterating sequence : list/array, string, tuple, set, dict

#list
list1 = list(("one","two","three","four"))
list2 = ["NL","BE","FR","DE","UK"]
print(type(list1))
print(type(list2))
for x in list1:
     print(x, type(x), len(x))

#string
string1 = "Hello Python"
for x in string1:
     print(x, type(x),len(x))

#break -> exit loop
print("break")
for x in list2:
     if x == "DE": break
     print(x)

#continue -> skip element but stay in loop
print("continue")
for x in list1:
     if x == "two": continue
     print(x)

#range starts @ 0
print("range(5)")
for x in range(5):
     print(x,type(x))

#range start,stop,step=1
print("range(3,9)")
for x in range(3,9):
     print(x, type(x))

#range start,stop,step
print("range(1,20,3)")
for x in range(1,20,3):
     print(x, type(x))

#else
print("else")
for x in range(1):
     print(x)
else:
     print("out of loop")

#else & break
print("break else")
for x in range(6):
     if x == 3 : break
     print(x)
else:
     print("out of loop")

#nested loops
print("nested")
i=1
for x in list1:
     for y in list2:
          print(i,x,y)
          i += 1

#pass
list3 = list()
print("pass ")
for x in list3:
     pass


