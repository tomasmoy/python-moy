from cmath import pi
from re import I


"""
import math
rad = float(input("Ingrese el radio del circulo:"))
area = pi * (math.pow(2,rad))
print(area, "cm2")
"""
"""
#n+nn+nnn
x = int(input("Ingrese numero"))
n1 = int("%s"%(x))
n2 = int("%s%s"%(x, x))
n3 = int("%s%s%s"%(x, x, x))
result = n1+n2+n3
print (result)
"""
"""
from datetime import date
fecha1 = date(2021,12,23)
fecha2 = date(2012,12,21)
resta = fecha1 - fecha2
print(resta.microseconds)
"""
def resta100(x):
    return ((abs(1000-x) <= 100) or (abs(2000-x) <= 100))

print(resta100(1000))
print(resta100(100))
print(resta100(950))