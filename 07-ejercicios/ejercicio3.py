
"""
Ejercicio3: Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales. Resolverlo con for y con while
"""

countF = 1

print("Los numeros cuadrados de 1 al 60 son: ")

for countF in range(1,61):
    print(f"El numero cuadrado de {countF} es: {countF*countF}")

print("Fin del bucle for")

countW = 1

while countW <= 60:
    print(f"El numero cuadrado de {countW} es: {countW*countW}")
    countW += 1

print("Fin del bucle while")
    
