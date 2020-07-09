class Person:

    def __init__(self,name,apell,edad):
        self.name = name
        self.apell = apell
        self.age = edad

    def mostrar(self):
        print(self.name,self.apell,f" usted tiene {self.age} años")


class Student(Person):
   ## the pass keyword when you do    not wantto add any other properties or methods tothe class
    pass

    def __init__(self,n,a,e,tel):
        Person.__init__(self,n,a,e)
        self.tel = tel

    def mostrar2(self):
       print("Herencia: ")
       Person.mostrar(self)
       print("Se telefono es: ",self.tel)






obj = Student("Luis","Valencia",19,"353-105-86-49")
obj.mostrar2()
obj.mostrar()

show = obj.mostrar2()

show



