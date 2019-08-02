x = {1,2,3,4,5,6,7,8,9,10}
x2 = set(range(0,20,2))


print(x | x2)
print(x & x2)
print(x2 & x)
print(x - x2)
print(x2 - x)


#def esPar(n):
 #   n = n.split(" ")
  #  for val in n:
   #     yield nint(val)%2==0


numbers = input("Ingrese números separados por espacios: ")
# Convertir a una lista de números enteros.
#numbers = [int(n) for n in numbers.split(" ") if n in esPar(numbers)]


print("Pares")
print(numbers)

#Dos conjuntos son iguales si y solo si contienen los mismos elementos (a esto se lo conoce como principio de extensionalidad):
print({1,2,3} == {1,3,2})#true
print({1,2,3} == {1,3,2,6})#false
print({1,2,3} == {1,2,3})#true