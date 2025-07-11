#using additional functionality outside functions is decorators.
#function will act as a decorator here,
from datetime import datetime
def decorator(fun):
    def wrapper():
        print("Before Calling Function")
        fun()
        print("After Calling Function")
    return wrapper

@decorator
def greet():
    print("hi Good Morning ") #whenever we call greet decorator gets called.

@decorator
def print_time():
    print(datetime.now())

greet()
print_time()
print("------------------------------------------------")

# DECORATOR FOR A FUNCTION WITH PARAMETERS AND A RETURN VALUE
def deco(f):
    def wrap(*args,**kwargs):
        print(f"before calling function {f.__name__}")
        result = f(*args,**kwargs)
        print(f"after calling function {f.__name__}")
        return result
    return wrap

@deco
def sum(a,b):
    # print(f"{a} + {b} = {a+b}")
     return a+b #none 
print(sum(10,20))

