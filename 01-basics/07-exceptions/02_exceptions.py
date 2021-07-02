import sys

# var not defined
try:
  print(x)
except NameError:
  print("Variable x is not defined")
  sys.exit(1)
except:
  print("Something else went wrong")