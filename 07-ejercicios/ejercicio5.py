
"""
Ejercicio 5: Hacer un programa que muestre todos los numeros
entre dos numeros que diga el usuario
"""

print("############## Numeros que se encuentran dentro de un rango #################")

numOne = int(input("Ingrese el número inicial: "))
numTwo = int(input("Ingrese el numero final: "))+1

if numOne < numTwo:
    for count in range(numOne, numTwo):
        print(count)
else:
    print("El numero 1 debe ser menor al numero 2")
        
