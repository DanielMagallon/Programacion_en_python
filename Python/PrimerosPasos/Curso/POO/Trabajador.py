from Curso.POO.Persona import *

class Trabajador(Persona):

    def __init__(self, nom, ap, edad, sex, num_seguro, ap2=None):
        Persona.__init__(self, nom, ap, edad, sex, ap2)
        self.seguro = num_seguro

    def mostrar(yeo):
        Persona.mostrar(yeo)
        print("Num seguro: ", yeo.seguro)
