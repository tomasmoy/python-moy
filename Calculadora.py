#Calculadora
print ("Calculadora")
print ("Seleccione la operación a realizar")
print ("1- Suma \n2- Resta \n3- Multiplicacion \n4- Division")
opcion = int(input(""))

if opcion == 1:
    print ("Ingrese el primer numero")
    num1 = float(input(""))
    print ("Ingrese el segundo numero")
    num2 = float(input(""))
    resultado = num1 + num2
    resultado = str(round(resultado,2))
    print ("El resultado es:", resultado)

elif opcion == 2:
    print ("Ingrese el primer numero")
    num1 = float(input(""))
    print ("Ingrese el segundo numero")
    num2 = float(input(""))
    resultado = num1 - num2
    resultado = str(round(resultado,2))
    print ("El resultado es:", resultado)

elif opcion == 3:
    print ("Ingrese el primer numero")
    num1 = float(input(""))
    print ("Ingrese el segundo numero")
    num2 = float(input(""))
    resultado = num1 * num2
    resultado = str(round(resultado,2))
    print ("El resultado es:", resultado)

elif opcion == 4:
    print ("Ingrese el primer numero")
    num1 = float(input(""))
    print ("Ingrese el segundo numero")
    num2 = float(input(""))
    resultado = num1 / num2
    resultado = str(round(resultado,2))
    print ("El resultado es:", resultado)
