from functools import wraps

dictr = {}

def save_value(func):
    @wraps(func)
    def wrapper(key, value):
        dictr.update({key: value})
        print("Your dicction: ", dictr)
        return func(key, value)

    return wrapper


@save_value
def setVal(key, value):
    print("setting")

setVal('1', 1)
setVal('2', 2)


def printArgs(func):
  def innerFunc(*args, **kwargs):
    print(args)
    print(kwargs)
    return func(*args, **kwargs)

  return innerFunc

#foobar: Función decorada
@printArgs
def foobar(x, y, z):
  return x * y + z

print(foobar(3, y=5, z=10))
# (3, 5)
# {'z': 10}
# 25 = 3 * 5 + 10

class Decorator(object):
  """Clase de decorador simple."""
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Antes de ser llamada la función.')
    retorno = self.func(*args, **kwargs)
    print('Despues de ser llamada la función.')
    print(retorno)
    return retorno

@Decorator
def function():
  print('Dentro de la función.')
  return "Retorno"

function()

def singleton(cls):
    instances = {}
    print("Singleton: ",cls)

    def get_instance(x):
        if cls not in instances:
            print("Returning new cls")
            instances[cls] = cls(x)
        return instances[cls]
    return get_instance


@singleton
class MyClass:

    def __init__(self,x):
        self.x=x


my = MyClass(20)
my2 = MyClass(10)

print("x on my: ",my.x)
print("x on my2: ",my2.x)
print("my.x = 1000 ")
my.x=1000
print("x on my: ",my.x)
print("x on my2: ",my.x)


class ErrorCheck:

    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !!")
        else:
            return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)


#  returns 6
print(add_numbers(1, 2, 3))

# raises Error.
print(add_numbers(1, '2', 3))
