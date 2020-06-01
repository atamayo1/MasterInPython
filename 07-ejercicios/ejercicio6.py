"""
Ejercicio 6: Mostrar todas las tablas de multiplicar del 1 al 10
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

for numCount in range(0, 11):
    print("#####################")
    print(f"Tabla del {numCount}")
    print("#####################")
    for count in range(1, 11):
        print(f"{numCount} x {count} = {numCount * count}")

