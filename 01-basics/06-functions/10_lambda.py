print("lambda +")
x = lambda a : a + 10
print(x(5))

print("lambda *")
x = lambda a, b : a * b
print(x(5, 6))

print("lambda +")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# usage in another function (nested function)
print("nested lambda using lambda double")
def multiply(n):
    return lambda a: a * n

double=multiply(2)
print("double -> ",double)
print(double(10))

triple=multiply(3)
print("triple -> ",triple)
print(triple(10))
