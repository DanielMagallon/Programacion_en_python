#!/usr/bin/env python
# coding: utf-8

# In[16]:


edad = 42
nombre="Yeo"
promedio=9.78
esPython=True
print("La edad de" ,nombre," es de ",edad," anios con promedio de ",promedio)

if(esPython):
    print("en el lenguaje python")
    
else:
    print("en otro lenguaje")
    print("como java,c++")

    print("\nAhora leeremos datos")
    print("\tPara leer dato se usa var_name = input(), lo que retornara una cadena, asi que para convertir a un numero por ejemplo se usa:\n")
    print("\tnum = input() --- num = int(num) o num = int(input)")
    print("\tSi no convertimos a numero y aplicamos una operacion sobre ella marcara error, a excepto de '*' ya que lo que hara es imprimir la cadena las veces que lo multiplques")
    print("Ingresa un numero: ")
    num = int(input())
    print("\tIngresa otro numero: ")
    num2 = input()
    num2 = int(num2)
    print("La suma es: ",(num+num2))

    print("\nIngresa a un dato: ")
    dato = input()
    print("Cuantas veces deseas concantenarlo/imprimirlo? ")
    n = int(input())

    print("Salida: ",dato*n)

    print("\n\n\t----------------------Divisas y Operadores Arimeticos--------------------------\n")

    print("Vamos a dividir el numero: ")
    num = float(input())
    print("entre el numero: ")
    num2 = float(input())
    print("La division de ",num,"/",num2,"=",(num/num2))
    
    a = 12
    b = 8
    c = 4.5
    print("a/b tipo float: ",a/b)
    print("a/b tipo int: ",int(a/b))
    print("a < 20  and b < 10",a<20 and b < 10)
    print("a < 4  or b <= 8",a<20 or b < 10)
        
    print("\n Para usar else if podemos usar else: (tabulador) if(condicion): o bien podemos hacer uso del elif(condicion):")
        
    if(a==11):
        print("a=12")
    else:
        if(b==8):
            print("b=8")
        elif(c==4.50):
            print("c fue = 4.5")
            print("b != 8")
            
        print("a fue != 12")
        

    print("\n\tUso del for")
    print("\t for i in range(valorinicial,valorfinal) o range(valorfinal) o rango(inicio,final,incremento(+,-)")
    print("Imrimir los numeros de x a y")    
    print("Dame x: ")
    num = int(input())
    print("Dame y: ")
    num2 = int(input())
    print("Dame el (in/de)cremento")
    inc = int(input())
    print("Salida: \n")



    for num in range(num,num2+inc,inc):
        if(num==10):
            print("Numero = 10")
            continue;
            
        print(num)
        
print("\n\tUso del while")
print("\tWhile(condicion):")

x = 0;


while(x<=10):
    print("x= ",x)
    x+=1

z = 5+1j
w = 6 + 8j
y = 6e3
d = 1e10
print(z+w)
print(y)
print(d)
f = 5 + 6j + 2j
print(z + f)

print(24//2)

    
print("fin del programa")

a,b = 10,20

print(a,"_",b)

# In[ ]:




