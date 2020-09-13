class A:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Aa():

    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age

class B(A,Aa):

    def __init__(self, name,age):
        A.__init__(self,name)
        Aa.__init__(self,age)

    def get_name(self):
        #Error : print("Im getting name with super().name ",super.name)
        print("Im getting name with self.name ", self.name)
        return super().get_name()


b = B("Edgar",10)
print(b.get_name())
print(b.get_age())
