
#El guion bajo aqui tambien es usado como variable, por lo que podemos tambien imprimir su valor
for _ in range(10):
    print("Hola")

def metodoClass(met,class_):
    pass

#Un solo guion bajo despues de un nombre: Para evitar conflictos con palabras clave
obj=None
#Si no usamos el guion en esta variable, el compilador de python lo tomara como una de sus palabras reservadas
metodoClass(class_="Hola",met=obj)

def claseInstanciada(func):
    def wrapper(self):
        print("Clase instanciada")
        return func(self)

    return wrapper

#El doble guion antes de una variable/metodo indica que esta sera privada

class GuionPrivado:
    __var=10

    @claseInstanciada
    def __init__(self):
        pass


    def __impirmir(self):
        print("Hola")


clase = GuionPrivado()
try:
    print(clase.__var)
except AttributeError:
    print("No existe la variable")

#clase.__impirmir()

obj = object

print(dir(obj))