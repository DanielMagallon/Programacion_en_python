class User:
    usuario=""
    __clave=""

    def __init__(self,user):
        self.usuario=user

    def setPass(self,passw):
        self.__clave=passw

    def getPass(self):
        return self.__clave

    def mostrar(self):
        print(f"Su usuario es {self.usuario} y su contrasenia es {self.getPass()}")
