movies = ["The Holy Grail","Avengers End Game","Avenger Infinity War"]

print("Movies 0: ",movies[0])
print("Movies 1: ",movies[1])
print("Movies 2: ",movies[2])

movies[0]="John Wick"

movies.append("Chucky")

print("Full list: ",movies)

print("Tamaño lista: ",len(movies))

valToRemove="John"

print("Removiendo {} {}....".format(valToRemove,",checking"))

if valToRemove in movies:
    movies.remove(valToRemove)
else:
    print("No existe {}".format(valToRemove))

valToRemove="John Wick"
print("Removiendo {} {}....".format(valToRemove,",checking"))

if valToRemove in movies:
    movies.remove(valToRemove)
else:
    print("No existe {}".format(valToRemove))

print("Full list: ",movies)

print("Sacando ultimo valor: {} ".format(movies.pop()))
print("Full list: ",movies)

print("Agregando mas items por arrays...")
movies.extend(["La Llorona","El aro"])

print("Agregando mas items por caracter...")
movies.extend("ABC")

print("Full list: ",movies)


movies.insert(1,"Maldicion")
print("Full list: ",movies)

print("Eliminando desde index 5")
del movies[5:]

print("Agregando años...")
years=[2019,2000,2018,1999,1997]

for i in range(0,len(movies),1):
    movies.insert(2*i+1,years[i])

# A B C
# 1 2 3
# A 1 B 2 C 3
# 0 -> A 1 B C= 1
# 1 -> A 1 B 2 C= 3
# 2 -> A 1 B 2 C 3= 5

print("Full list: ",movies)

[print(i) for i in ["1","2","3"]]