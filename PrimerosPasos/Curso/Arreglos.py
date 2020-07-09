calificaciones = {"Luis":3,"Manuel":2,1:"Pedro"} #set
alumnos = ["Juan","Pedro","Daniel","Javier","Lalo"] #list

#Las llaves de rizo {} crean dictionaries o sets. Los corchetes crean lists.


print(calificaciones["Luis"])
print(calificaciones[1])
print(alumnos)

x = 4
d = 2
if x >= 2 and d>=2:
    print("d")

if(x<2<5):
    pass

if "Juan" in alumnos:
    print("Esta juan en los alumnos")

for val in calificaciones:
    print(f"Key: {val} with valor {calificaciones[val]}")

print("\nAlumnos: ")
for val in alumnos:
    print(val)

alumnos[0] = ["d","a","d"]

print(alumnos[0])
print(alumnos[0][0])
print(alumnos[0][1])

print(alumnos)
print(f"arregl alumnos contiene {len(alumnos)} elementos")
print(f"La posicion 0 de alumnos contiene {len(alumnos[0])} elementos")

print(alumnos[0:2])
print(alumnos[0][0:2])
print(alumnos[2:])
print("Borrando la lista")
alumnos[:] = []
print(alumnos)
alumnos = ["Pedro","Juan",calificaciones]
print("Anidando alumnos y calficaciones",alumnos)

lista = ["Juan",1,4.5]
lista2 = [1,2,3,5,2,2]
print(lista)
print("Añadiendo Luis...")
lista.append("Luis")
print(lista)
print("Limpiando lista con clear")
lista.clear()
print("lista: ",lista)
lista = lista2.copy()
print(lista)

print("Lista2.extends  = agrega mas de un elemento de putazo")
print(lista2)
lista2.extend([20,30,])
print(lista2)
lista2.insert(1,1.5)
print(lista2)
print(f"count of 2 in lista2: {lista2.count(2)}")
print("Ordenando lista")
lista2.sort()
print(lista2)

listastr = ["Juan","Danie","Ariel","Water"]
print(listastr)
listastr.reverse()
print("reversa: ",listastr)
listastr.sort()
print("Lista ordenda: ",listastr)
del listastr[0]
del listastr[0]
listastr.remove("Juan")
print(listastr)
listastr.pop()
print(listastr)

for cad in "banana":
    print(cad)

car1 = "corvete"
car2 = "viper"






