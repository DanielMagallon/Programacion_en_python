class Persona:

#Usando una variale como global no sera reconocida por el argumento self.varuable
#Usar self.atriuto o nombreClase.atrbuto es distinto, Persona. lo hace estatico, y self. es dinamico

    name=""
    ap1=""
    ap2=None
    edad=0
    instancias=0

    def __init__(self,nom,ap,edad,sex,ap2=None):
        self.name=nom
        self.ap1=ap
        self.ap2=ap2
        self.edad=edad
        self.sex = sex
        Persona.instancias+=1

    def mostrar(yeo):
        print("Nombre: ",yeo.name)
        print("Apellido Paterno: ",yeo.ap1)

        if(yeo.ap2!=None):
            print("Apellido Materno: ",yeo.ap2)

        print("Sexo: ",yeo.sex)

        print("Edad: ",yeo.edad)

    def countInstance(self):
        print("Instancias = #", Persona.instancias)

    @staticmethod
    def staticCountInstance():
        print("Instancias: ",Persona.instancias)


