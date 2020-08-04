global constantePI, a, x
constantePI = 3.1415


def writemsg(st):
    print("Hola " + st)
    global b
    b = " 51"
    print("PI vale: ", constantePI)


def sobrecargaMetodo(n, n2=1):

    print("\t\t\t\t",b)
    return n + n2


def multipleParameter(*args):

    size = len(args)
    print("Argumentos totales: ", size)
    for i in range(size):
        print(args[i])


def usoInstanceOf(*args):
    for obj in range(len(args)):
        if (isinstance(args[obj], str)):
            print(args[obj], " es una cadena")
        elif isinstance(args[obj], int):
            print(args[obj], " es un entero")

        else:
            print(args[obj], " no se que sea eso")

def recursive(val):
    if(val!=0):
        print(val)

        recursive(val-1)
        print(val)

#va retornando elementos
def usoYield(max):
    cont=1

    while cont<=max:
        yield cont
        print("Itere: ",cont)
        cont += 1


def foo():
    x = 2
    # eval (codigo a evauluar,v1,v2) donde v1 puede ser locals() o globals() y v2 debe ser el opuesto de  v1, en este
    # caso si existen dos variables iguales de nombre, el v1 tendra mas prioridad para efecutar la operacion sovre la varable coressp.
    y = eval("a + 1 + x", locals(), globals())
    print("y=", y)
    y = eval("a + 1 + x", globals(), locals())
    print("y=", y)


print("Creand y llamando funciones")
a = x = 100
writemsg("mundo")
print(b)

# Podemos sobrecargara metodos, basta con darles valores default a un parametro
print(sobrecargaMetodo(5, 5))
print(sobrecargaMetodo(25))

print("\n\tUsando la funcion eval(...)")
print(globals()["constantePI"])
foo()

multipleParameter("Hola", "Mudo", 4, True)
print("\nUso isinstance")
usoInstanceOf(False, True, 45.4, "Hola", 'Puto', 'c', 1);
print("Recursion: ")
recursive(10)

print("Suma: ")
print(sobrecargaMetodo(n2=20,n=10))

def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- ¿Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)

    for arg in argumentos:
        print(arg)
    print("-" * 40)
    for c in palabrasclaves:
        print(c, ":", palabrasclaves[c])

ventadequeso("Limburger", ["Jaun"],
             cliente="Juan Garau",
             vendedor="Miguel Paez",
             puesto="Venta de Queso Argentino")

def loro(tension, estado='rostizado', accion='explotar'):
       print("-- Este loro no va a", accion, end=' ')
       print("si le aplicás", tension, "voltios.", end=' ')
       print("Está", estado, "!")

d = {"tension": "cinco mil", "estado": "demacrado",
     "accion": "VOLAR"}
loro(**d)

print("Uso del yield")
for it in usoYield(10):
    print(it)

def metodo():
    print("Metodo")

def metodo():
    print("Method")

metodo()

