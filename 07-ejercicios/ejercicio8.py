"""
Ejercicio 8: ¿Cuanto es el X por ciento de X número?
Ejemplo: ¿Cuanto es el 20% de 150?
"""

num = int(input("Ingrese el número al cual quiere sacar el porcentaje: "))
numPercent = int(input(f"¿Que porcentaje quiere sacar de {num}?: "))

if numPercent <= 100:
    print(f"El {numPercent}% de {num} es = {int(num*(numPercent/100))}")