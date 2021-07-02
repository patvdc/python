# integer -> whole number
integer_number1 = 5
integer_number2 = -205
print("int1 =",integer_number1,"\tint2 =",integer_number2)

# float -> decimal number
float_number = 2.0
float_number2 = -32.54e10
print("float1 =",float_number,"\tfloat2 =",float_number2)

# complex -> j = imaginary part
complex_number = 3.14j
print("complex =",complex_number)

# casting to int
a = int(3)
b = int(3.33)
c = int("3")
print("casting to int -> ","int(3) =",a,"\tint(3.33) =",b,"\tint('3') =",c)
#c = int("3.14") #ValueError: invalid literal for int() with base 10: '3.14'

# casting to float
a = float(3)
b = float(3.33)
c = float("3.1416")
print("casting to float -> ","float(3) =",a,"\tfloat(3.33) =",b,"\tfloat('3.1416') =",c)

# data type of a var
print("data type -> ","type(a) =",type(a),"\ttype(b) =",type(b),"\ttype(c) =",type(c))

# one line assignment

x,y,z = 2,4,6
print(f"one line assignment -> ","x =",x,"\ty =",y,"\tz =",z)

print("counting")
# arithmetic operators (counting)
f = 7
g = 3
print("f = ",f,"\tg = ",g)

# sum
print("sum","f + g","->",f + g)
print("sum","2 + 2","->",2 + 2)
print("sum","2 + 2","->","2 + 2")

# subtract
print("subtract","f - g","->",f - g)

# multiply
print("multiply","f * g","->",f * g)

# division
print("division","f / g","->",f / g)
# modulus
print("division remainder","f % g","->",f % g)
# floor division (round to nearest int)
print("division nearest int","f // g","->",f // g)

# exponential
print("exponential","f ** g","->",f ** g)

# assignment operator
print("assignment","x = 5","->",x)

# same as x=x+1
x+=1
print("increment","x += 1","->",x)

# same as x=x-1
x-=1
print("decrement","x -= 1","->",x)

# same as x=x*3
x*=3
print("multiply","x *= 3","->",x)

# /=  %=  //=  **=  &= !=  ^=  >>=  <<=

# compare operator
print("compare")
a = 7
b = 10
print("a =",a,"\tb =",b)

print("equal"," a == b"," -> ", a == b)
print("gt"," a > b"," -> ", a > b)
print("lt"," a < b"," -> ", a < b)
print("ltae"," a <= b"," -> ", a <= b)
print("gtae"," a >= b"," -> ", a >= b)
print("not equal"," a != b"," -> ", a != b)

# logical operator
print("logical")
x = 2
print("x =",x)
# and
print("and -> ","x < 5 and x < 10"," -> ",x < 5 and x < 10)
# or
print("or -> ","x < 5 or x < 10"," -> ",x < 5 or x < 10)
# not
print("not -> ","not(x < 5 and x < 10)"," -> ",not(x < 5 or x < 10))

# instance of a class
print("instance of a class -> ","isinstance(x,int)"," ->",isinstance(x,int))
























