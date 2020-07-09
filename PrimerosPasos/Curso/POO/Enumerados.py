lenguajes = ["Java","Python","C++","PHP"]

lista = list(enumerate(lenguajes,5))

print(type(lista[0]))
print(lista)

letras="abcdefghijklmnñopqstuvwxyz"

for index,caracter in enumerate(letras,1):
    print(index,caracter)

tupla = (1,2,3)


#a,b,c=tupla tamien es valido
(a,b,c) = tupla

print(a,b,c)

for t in enumerate(lenguajes,10):
    print(t)

for t in enumerate(lenguajes,10):
    index = t[0]
    valor = t[1]
    print('%d = %s'%(index,valor))