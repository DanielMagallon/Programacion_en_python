class MyClass:

    def __init__(s,name,age):
        s.name = name
        s.age = age

    def mostrar(self):
        print(self.name,f"usted tiene {self.age}")

miclase = MyClass("Felipe",34)
print(miclase.name)
print(miclase.age)
miclase.mostrar()
miclase.age=10
miclase.mostrar()
print(miclase)
del miclase.age
miclase.mostrar()