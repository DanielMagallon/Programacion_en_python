#needs to install "pip install multipledispatch"
from multipledispatch import dispatch

from functools import  wraps

@dispatch(int, int)
def agrega(a, b):
    return a + b

@dispatch(str,str)
def agrega(a,b):
    return "-".join((a,b))

print(agrega(1, 5))
print(agrega("Hola","Mundo"))

def debug(function):
    wraps(function)
    def newFunction(*args,**kwargs):
        print(f"Function {function.__name__}() called!")
        return function(*args,**kwargs)
    return newFunction

@debug
def add(a,b,**dics):
    for i in dics:
        print(i+": "+dics[i])
    return a+b

@debug
@dispatch(int)
def neg(n):
    return n*-1

print(add(6,5,op="Suma",op2="resta"))
print(neg(4))
print(neg.__name__)
help(neg)

def fa(message="Hello", name=None):
     print("{0}, {1}!".format(message, name))

kwargs = {"message": "Hola", "name": "mundo"}

fa(**kwargs)



