
"""

FOR

con el break -> puedes parar el bucle

"""

print("Bucle FOR")

count = 0
result = 0

for count in range(1, 6):
    print("voy por el "+ str(count))

    result += count

print(f"El resultado es: {result}")

print("################ Ejemplo ################")

numUser = int(input("¿De que número quieres la tabla?: "))

if numUser < 1:
    numUser = 1

print(f"###### Tabla de multiplicar del número {numUser} ####")

for numTable in range(1, 11):
    print(f"{numUser} x {numTable} = {numUser * numTable}")

else:
    print("Tabla finaliza.")
