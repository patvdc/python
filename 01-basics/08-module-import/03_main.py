from modules import square

print("from import")
for i in range(10):
    print(f"square of {i} = {square(i)}")


# import whole module
import modules

print("import")
for i in range(10):
    print(f"square of {i} = {modules.square(i)}")

