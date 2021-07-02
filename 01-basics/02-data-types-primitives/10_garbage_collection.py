# garbage collection (normally done by python automatically)
x = 1
y = 2
print(x,y)
del x,y
#print(x,y)
#NameError: name 'x' is not defined
#IndentationError: unexpected indent