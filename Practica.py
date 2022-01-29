"""
print ("Detector de par o impar")
numero = int(input("Inserte un numero del 1 al 1000"))
if numero == 0:
    print ("Este numero es par")
elif numero%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")

"""
"""
print ("Contador de letras")
palabra = str(input("Escriba una frase"))
conteo = len(palabra)
print ("Su frase tiene", conteo, "letras")

"""
"""
print ("Sumar")
x = int(input("Inserte el primer numero"))
y = int(input("Inserte el segundo numero"))
suma = x + y
print ("El resultado es", suma)

"""

"""
print ("Funcion max")
def max(numero1, numero2):
    if numero1 > numero2:
        print (numero1)
    else:
        print (numero2)
    return
max(1,28)

"""
"""
a = ["Fideos", "Bananas", "Manzanas"]
for i in range (len(a)):
    print (a[i])
    print (i)

"""
"""
num = int(input("Ingrese su numero"))
if num > 0 and num < 10:
    print("Entre 0 y 10")
elif num > 11 and num < 20:
    print("Entre 11 y 20")
elif num > 21 and num < 30:
    print("Entre 21 y 30")
else:
    print("Fuera del intervalo")

"""
"""
x = "Hola mundo"

for i in range (len(x)):
    print (x[i])

"""
"""
for i in range (1,101):
    if ((i%2) == 0):
        print(i)
"""
"""
def num_max(a, b, c, d):
    if a > b and a > c and a > d:
        print(a)
    elif b > a and b > c and b > d:
        print(b)
    elif c > a and c > b and c > d:
        print(c)
    elif d > a and d > b and d > c:
        print(d)
    else:
        print("Son iguales")

num_max(1,1,1,1)
"""
"""
def num_max_min(a, b, c):
    if a > b and a > c:
        print ("El numero mayor es", a, "Y el menor es", b)
    elif b > a and b > c:
        print ("El numero mayor es", b, "Y el menor es", c)
    elif c > a and c > b:
        print ("El numero mayor es", c, "Y el menor es", a)
    else:
        print("Los numeros son iguales")

num_max_min(11,11,11)

"""