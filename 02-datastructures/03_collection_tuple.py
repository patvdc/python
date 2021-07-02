# tuple () : collection data type
# ordered, immutable (read-only list), duplicate elements allowed

# create empty tuple
empty_tuple1 = ()
print("empty tuple\t\t",empty_tuple1)

# create empty tuple using constructor
empty_tuple2 = tuple()
print("empty tuple\t\t",empty_tuple2)

color_tuple = tuple(("green","yellow","white","black","red"))
print("color tuple\t\t",color_tuple)

# same data types with duplicates
string_tuple = ("John", "Mike", "pat","Zorba","Sandra","Kelly", "Mike","Anna","Brian")
print("string tuple\t",string_tuple)

# different data types
mixed_tuple = ("Peter", "Smith", 34, True, "male")
print("mixed tuple\t\t", mixed_tuple)

# tuple with 1 item -> comma !!!
one_tuple = ("python",)
print("one tuple\t\t", one_tuple ,"\t",type(one_tuple))
# one_tuple = ("python")    not okee

# unpack tuple elements into string + type class + *
print("unpack")
a,b,c,d,e = color_tuple
(f,g,h,*i) = color_tuple    #rest of values
print(type(color_tuple))
print(a,"->",type(a),"\t",b,"->",type(b),"\t",c,"->",type(c))
print(f,"->",type(f),"\t",g,"->",type(g),"\t",h,"->",type(h))
(first,*middle,last) = color_tuple   # *middle = list
print(first,"->",type(first),"\t",middle,"->",type(middle),"\t",last,"->",type(last))

# length
print("len","\t\t",len(color_tuple))

# slicing first elements
print("first element\t",color_tuple[0])

# slicing last elements
print("last element\t",color_tuple[-1])

# slicing ange of elements (sub-tuple)
print("range elements\t",color_tuple[1:3])
print("range elements\t",color_tuple[-3:])

# iterate for each
print("loop for each")
for s in color_tuple: print(s, "\t", type(s))

# loop index
print("loop index")
for i in range(len(color_tuple)):
    print(color_tuple[i],"\t", type(color_tuple[i]))

# present
if "black" in color_tuple:
    print("present in tuple")
else:
    print("not present in tuple")

# add item using index
print("add item using list index")
print(string_tuple)
y = list(string_tuple)
y[0] = "oak"
string_tuple = tuple(y)
print(string_tuple)

# add item using list append
print("add item using list append")
print(string_tuple)
y = list(string_tuple)
y.append("ubuntu")
string_tuple = tuple(y)
print(string_tuple)

# append tuple with tuple
print("concat 2 tuples")
print(string_tuple)
print(color_tuple)
string_tuple += color_tuple
print(string_tuple)

# join 2 tuples into 3th using +
print("join 2 tuples into 3th")
print(color_tuple)
print(one_tuple)
tuple_final = color_tuple + one_tuple
print(tuple_final)

# multiply tuple
print("multiply tuple")
print(one_tuple)
new_tuple = one_tuple * 4
print(new_tuple)

# present using index
print("present using index")
x = color_tuple.index("black")
print(x)

# remove item using list
print("remove item using list")
print(string_tuple)
y = list(string_tuple)
y.remove("Mike")
string_tuple = tuple(y)
print(string_tuple)

# delete tuple
print("delete tuple")
print(color_tuple)
del color_tuple
#print(color_tuple)    NameError: name 'color_tuple' is not defined

#join tuple into str
print("tuple join into str")
a_tuple = ("Alpha","Beta","Gamma")
x = "#".join(a_tuple)
print(x)   # Alpha#Beta#Gamma
