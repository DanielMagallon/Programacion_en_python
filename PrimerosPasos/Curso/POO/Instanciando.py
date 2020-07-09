from Curso.POO.Auto import Carro,Auto
from Curso.POO.Encapsulamiento import User
from Curso.POO.Persona import *
from Curso.POO.Trabajador import *

us = User("Yeo99")
us.setPass(12345)
us.mostrar()

person = Persona("Edgar","Magallon",20,"Masculino")
person2 = Persona("Luis","Valencia",19,"Femenino","Figueroa")
person3 = Persona("Luis","Valencia",49,"Femenino")

Persona.countInstance(Persona)
Persona.staticCountInstance()

from Curso.POO import DeclaracionVariables

lucas = DeclaracionVariables.Perro("Lucas")
zeus = DeclaracionVariables.Perro("Zeus")


lucas.agregaTruco("Gira")
zeus.agregaTruco("Camina en dos patas")
zeus.agregaTruco(1)
print(zeus._name)
print(lucas._name)


zeus.showTrucos()
lucas.showTrucos()

print("\n\tPolimorfismo")

people = (User("Juan"),Persona("Pollo","Bautista",17,"Masculino"),person,person2,person3)

people[0].setPass("enchiladas99")
Persona.staticCountInstance()

for ins in people:
    ins.mostrar()

tr = Trabajador("Juan","Luz",56,"Masculino",1020012)
tr.mostrar()

if(False):
    auto = Auto()
    auto.color = "Rojo"
    auto.modelo = "Exotic"
    auto.marca = "Lamborguini"
    auto.velocidad = 394

    print(f"El auto {auto.marca} es un modelo {auto.modelo} que llega a una velocidad de {auto.velocidad} y "
          f"su color general es {auto.color}")

    car2 = Carro
    car2.color = "Amarillo"
    car2.color = "Challenger"
    car2.modelo = "Corvete"
    car2.puertas = "4"
    car2.velocidad = 400
    car2.mostrarDatos(car2)
    car2.acelerar(car2, 420)

    car = Carro("Lamborguini", "Rojo", "Exotic", 2, 390)
    car.mostrarDatos()
    car.acelerar(390)