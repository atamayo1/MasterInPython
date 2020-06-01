"""
Ejercicio 9: Hacer un programa que pida números indefinidamente,
hasta que coloque el numero 111
"""
print("Para parar el ciclo escriba el numero 111")
num = 1
while num != 111:
    num = int(input("Ingrese un número: "))
    if num == 111:
        print(f"El numero ingresado es -> {num} fin del ciclo")
        break
    else:
        print(f"El numero ingresado es -> {num}")
