class PruebaStatic():
    instancias = 0

    def __init__(self):
        PruebaStatic.instancias += 1

    @staticmethod
    def show():
        print(PruebaStatic.instancias)


PruebaStatic().show()
PruebaStatic().show()
PruebaStatic().show()

PruebaStatic.show()
