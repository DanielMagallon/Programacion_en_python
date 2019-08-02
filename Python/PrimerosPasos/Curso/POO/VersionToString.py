

class Time:


#Metodos magicos = __nobremetodo__

      def __init__(self,h=0,m=0,s=0):
          self.h = h
          self.m = m
          self.s = s

      def __repr__(self):
          return f"{self.h:02}:{self.m:02}:{self.s:02}"

tiempo = {'h':10,'m':20,'s':12}


ti = Time(**tiempo)
print(ti)

ti.h="100"

print(ti)