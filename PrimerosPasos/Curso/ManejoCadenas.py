cadena="hola como estas"
ca = "hola como estas?"
element = None;

if(element == None):
    print(element)
element = 4
if(element is 4): print("element is 4?",element is 4)

print("cadena1 in cadena2 itera y determina si contiene la cadena1 en la cadena 2")
if("hola" in "hola puto"):
    print("Cadena correcta")
    

if(not cadena is ca):
    print("cadena is not ca")
   
##cadena = ca
if(cadena is ca):
    print("cadena is ca")
    
else:
    print("cadena: ",cadena)
    print("cadena.capytalize() devuelve la cadena con la primera en mayusculas")
    cadena = cadena.capitalize()
    print(cadena)
    print("len(cadena) = ",len(cadena))

    print("cadena.center(n) 0 cadena.center(n,caracerrelleno) centra la cadena n espacios despues del cursor/le da un tamanio a la cadena de n (un tabulador)")
    cadena = cadena.center(50,'*')
    print(cadena)

    print("cadena.count(subCadena,deDonde, aDondeInnicar) = ",cadena.count("o"))
    print("\"12345\".isalnum() si todos los caracteres son alfanumericos = ","12345".isalnum());
    print("\"AHola2\".isalnum() si todos los caracteres son alfanumericos = ","AHola2".isalnum());
    print("\"123.45\".isalnum() si todos los caracteres son alfanumericos = ","123.45".isalnum());

    print("\"123.45\".isdigit() si todos los caracteres son numericos = ","123.45".isdigit());
    print("\"10\".isalnum() si todos los caracteres son numericos = ","10".isdigit());
    print("\"AF\".isalnum() si todos los caracteres son numericos = ","AF".isdigit());
    print("cadena.islower() todos los caracteres estan en minusculas? ",cadena.islower())
    cadena = ca
    print("cadena.islower()",cadena.islower())
    print("\"hola.upper()\" = ","hola".upper())
    print("\"vata pendejo.replace(a,e)\"","vata pendejo ".replace("a","e"))
    print("cadena[3] = ",cadena[3])
    print("cadena[0:4] = " ,cadena[0:4])
    print("\"Hola Perr1O.swapcase()\"=","Hola Perr1O".swapcase())
    print("\"conviertiendo a formato de tittulo\".title()","conviertiendo a formato de tittulo".title())
    print("\ncadena.ljust(espacios,carcterrelleno) ajusta a la izquierda: ","hola".ljust(40,"+"))
    print("\ncadena.rjust(espacios,carcterrelleno) ajusta a la derecha: ","hola".rjust(40,"+"))
    num = 1570;
    print("valor a cadena: str(numero)")
    print(str(num).zfill(10))
    cadena= "       hola como estas¡ "
    print(cadena)
    print("cadena.strip() elimina espacios vacios del inciio y final de la cadena: -",cadena.strip())
    
    print("\n\tDando formato con format()")
    cadena = "I want {2} but i dont have {0} because I'm so {1}"
    print(cadena.format("money","poor","a guitar"))
    
    d = 2;
    print(f"Hola {d**4}")
    
    
    print("///".join("hola mundojotos"))
    

