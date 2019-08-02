import time

_author_ = 'yeo'


class Auto:
    pass

class Carro:
    marca = ""
    color = ""
    modelo = ""
    puertas = 0
    costo=0.0

    def __init__(self, marca, color, model, puertas, vel, costo=15002400):
        self.marca = marca
        self.color = color
        self.modelo = model
        self.puertas = puertas
        self.vel = vel
        self.costo = costo

    def mostrarDatos(self):
        print(f"El auto {self.marca} es un modelo {self.modelo} que llega a una velocidad de {self.velocidad} y "
              f"su color general es {self.color} y cuenta con {self.puertas} puertas y cuesta {self.costo}$")

    def acelerar(self, vel):
        for i in range(10, vel, 50):
            print(f"El carro {self.marca} esta acelerando a una velocidad de {i} km/h")
            time.sleep(1)



