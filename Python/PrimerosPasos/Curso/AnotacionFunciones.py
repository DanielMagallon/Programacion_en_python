def recibeStringRetornaEntero(num_cad: str = "10") -> int:
    print("Anotaciones:", recibeStringRetornaEntero.__annotations__)
    return int(num_cad)


def showList(elemento, lista=[]):
    lista.append(elemento)
    print(lista)


def esMayor(x, y) -> str:
    return str(x) + " es mayor" if (x > y) else str(y) + " es mayor"

def retornoMultiple():
    return 1,2,"Hola",["Juan",2,5.4]

print(recibeStringRetornaEntero(12.2) + 2)
showList(10)
showList("20f")
showList(True
         )
showList('10.2')


print(esMayor(5, 5.5))
num,num2,c,lista = retornoMultiple()

print(num)
print(num2)
print(c)
print(lista)

print(type(lista))