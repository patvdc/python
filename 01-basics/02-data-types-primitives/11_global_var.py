# local/global scope/var

def myfunc():
    global language
    language = "python"

myfunc()
print("a computer language -> " + language)

# local var overruled by global var
language = "java"
def myfunc():
    global language
    language = "python"

myfunc()
print("a computer language -> " + language)


