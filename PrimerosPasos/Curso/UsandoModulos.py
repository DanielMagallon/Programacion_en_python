from Curso.Modules import myModules
from Curso.Modules.Math import Area
import math
from math import factorial

#import a,b,c


print(myModules.mathPow(2,2))
myModules.writeMsgs("Hola","Mundo")
Area.area(40,2)

x = 5
y = -8
z = 39.67
v = 6

res = x**2


print(f"{x}² = {res}")
print(f"tang({z}) = ",math.tan(z))
print(f"facotrial de {v} = ",factorial(v))
print(f"valor absoluto de {y} = ",math.fabs(y))

