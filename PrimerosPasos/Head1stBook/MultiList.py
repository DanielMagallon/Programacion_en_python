from Curso.Modules import myModules as m

movies=["Avengers: End Game",["El aro",["1999","Erick"]],["The Witch",["2010","Noan"]]]

print("{} made by {} in {}".format(movies[2][0],movies[2][1][1],movies[2][1][0]))

print(m.itemPerItem.__doc__)
m.itemPerItem(movies)

#Page 43 create a distribution (like a jar)