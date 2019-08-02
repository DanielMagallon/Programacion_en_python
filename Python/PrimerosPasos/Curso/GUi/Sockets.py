import socket

s = socket.socket()
s.connect(("localhost", 9999))

while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mensaje = input("Mensaje a enviar >> ")

    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    s.send(mensaje)

    #Si por alguna razon el mensaje es close cerramos la conexion
    if mensaje == "close":
        break

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Adios.")

#Cerramos la instancia del objeto servidor
s.close()