# announce function = decorator
def announce(f):
    def wrapper():
        print("Enter wrapper function")
        f()
        print("Exit wrapper function")
    return wrapper

@announce
def hello():
    print("hello world")

hello()