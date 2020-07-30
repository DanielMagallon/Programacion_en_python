import numpy
from time import perf_counter as pc
import random

a = numpy.arange(12)
print("a: ",a)

print("type(a): ",type(a))
print("a.shape: ",a.shape)
a.shape = 3,4
print("a.shape = 3,4 : \n\t",a)
print("a[2]: ",a[2])
print("a[2][2]: ",a[2][2])
print("a[2,2]: ",a[2,2])
print("a[:,1]: ",a[:,1])

print("a.transponse(): ",a.transpose())

