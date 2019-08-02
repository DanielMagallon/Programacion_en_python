import Curso.POO.NotIntegerException as notI
from functools import wraps

def _int_required(func):
    @wraps(func)
    def wrapper(self,value):
        if not isinstance(value, int):
            raise notI("A integer is required")
        return func(self,value)
    return wrapper

def _time_required(func):
    @wraps(func)
    def wrapper(self,other):
        if not isinstance(other,Time):
            raise TypeError("Solo se puede comparar entre objetos del Tipo Time")
        return func(self,other)



    return wrapper
#
    #__lt__() para a < b.
    #__gt__() para a > b.
    #__le__() para a <= b.
    #__ge__() para a >= b.
    #__ne__() para a != b.
    #__eq__() para a == b.
#

class Time:

#Metodos magicos = __nobremetodo__ son llamados automaticamennte cuando se hace uso de ciertas instrcciones como
# (>,>=,<=,==,!=,al instancias una clase )

      def __init__(self,h=0,m=0,s=0):
          self.h = h
          self.m = m
          self.s = s

      @property
      def hour(self):
          return self.h

      @hour.setter
      @_int_required
      def setHour(self,value):
          self.h = value


      @property
      def minute(self):
        return self.m

      @minute.setter
      @_int_required
      def set_minute(self,minute):
          self.m = minute


      def __repr__(self):
          return f"{self.h:02}:{self.m:02}:{self.s:02}"

      @_time_required
      def __eq__(self, other):

          return self.hour == other.hour and  self.minute == other.minute and self.s == other.s


t2 = Time(10,24,9)
t3 = Time(10,24,9)

print(t2==t3)



