class Perro:

    _name=""

    #Forma incorrecta de declarara una lista dependiente de cada instancia de la clase
    #trucos = []


    def __init__(self,name):
        self._name=name
        #Forma correcta de declarara un arreglo para cada instacnia de la cclase, asi no se vera afectada cuando se genere
        #una  nueva instancia
        self.trucos = []

    def agregaTruco(self,truco:str):
        self.trucos.append(truco)

    def showTrucos(self):
        print(self.trucos)

