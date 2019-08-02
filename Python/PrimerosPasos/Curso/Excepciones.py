
def div(n1,n2):
    if(n2==0):
        raise ZeroDivisionError("No se puede  dividir entre 0 papu")
    return n1/n2

try:
    div(4,0)
except ZeroDivisionError as zde:
    print(zde)

try:
    print(7/2)
    print(7/0)

#except ArithmeticError:
 #   print("No se puede dividir entre 0")
except ZeroDivisionError:
    print("No se puede dividir entre 0")

try:
    print(aa)
except NameError:
    print("aa is not defined")

try:
    print("Introduza un numero: ")
    #a = int(input())
    print(f"Ingresaste: {int(input())}")

except ValueError:
    print("Value error")
else:
    print("no hubo error al leer")

try:
    print("Introduza un numero: ")
    #a = int(input())
    print(f"Ingresaste: {float(input())}")

except KeyboardInterrupt:
    print("Se interrumpio la ejecucion")
except:
    print("Error")


a = -1
print("Yes") if a>=2 else print("Nope")

