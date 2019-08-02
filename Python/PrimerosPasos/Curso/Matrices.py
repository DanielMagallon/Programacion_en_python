import random

matriz = [ [1,2,3,[-1,-2]],
           [9,8,7],
           [10,20,30,40]]

print(matriz)

if [10,20,30,40] in matriz:
    print("El [10...]estan en la matriz")

if 1 in matriz[0]:
    print("Esta el 1 en matriz[0")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print("\n")

for mat in matriz:
    print(mat)


print("\n\tAlearios: ")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = random.randrange(5,11)

print(matriz)


