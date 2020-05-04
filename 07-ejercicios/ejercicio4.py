
"""
Ejericio 4: Pedir dos numeros al usuario y hacer todas las
operaciones basicas de una calculadora y mostrarlo en pantalla
"""

print("############## Operaciones basicas #############")

print("¿ Que operacion desea realizar Suma(+) , Resta(-) , Multiplicación(x)\
 , División(/) ?")

operacion = input("Coloque la operacion, es decir lo que aparece en parentesis: ")

numUser1 = int(input("Ingrese el primer numero: "))
numUser2 = int(input("Ingrese el segundo numero: "))

if operacion == "+":
    print(f"Suma de {numUser1} + {numUser2} = {numUser1+numUser2}")
elif operacion == "-":
    print(f"Resta de {numUser1} - {numUser2} = {numUser1-numUser2}")
elif operacion == "x":
    print(f"Multiplicación de {numUser1} x {numUser2} = {numUser1*numUser2}")
elif operacion == "/":
    print(f"División de {numUser1} / {numUser2} = {numUser1/numUser2}")
