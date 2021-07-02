# loop as long as condition = true, counter

# basic increment
print("basic increment")
i = 1
while i < 10:
    print(i)
    i += 1

# basic decrement
print("basic decrement")
i = 10
while i > 0:
    print(i)
    i -= 1

# using break to exit loop
print("break")
i = 1
while i < 10:
    print(i)
    if i == 5: break
    i += 1

# using continue to skip step
print("continue")
i = 0
while i < 10:
    i += 1
    if (i == 5) or (i == 7) : continue
    print(i)

# using else
print("continue")
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("loop ended")

# nested loop
print("nested loop")
l1 = list(("one","two","tree"))
print(type(l1))

# array 4x2
i = 1
while i < 5:
    j = 1
    while j < 3:
        print(i,j)
        j += 1
    i += 1

# random
import random
print("random")
position = None
# will run at least once
while position != 1:
    position = random.randint(1, 10)
    print(position)
