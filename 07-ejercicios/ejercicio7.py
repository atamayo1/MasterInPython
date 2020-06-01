"""
Ejercicio 7: Mostrar todas los numeros impares
entre dos numeros que decida el usuario
"""
print("Escriba los numeros entre los que quiere ver los números impares")
numOne = int(input("Ingrese el primero número: "))
numTwo = int(input("Ingrese el segundo número: "))
print("#####################################")
print("La lista de numeros a continuación son impares")
print("#####################################")

if numOne > numTwo:
    for element in range(numOne, numTwo+1):
        if element % 2 != 0:
            print(f"{element} es impar")
else:
    print("El número 1 debe ser mayor al número 2")