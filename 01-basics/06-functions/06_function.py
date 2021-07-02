# return value

def square(x):
  return x * x

print(square(3))
print(square(5))
print(square(9))

for i in range(11):
  print(f"Square of {i} = {square(i)}")