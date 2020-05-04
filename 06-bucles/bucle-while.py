
"""

While

"""


count = 1
while count <= 100:
    print(f"Estoy en el numero: {count}")
    count += 1


print("########### Example ############")

numUser = int(input("¿De que número quieres la tabla?: "))

if numUser < 1:
    numUser = 1

countTable = 1
while countTable <= 10:
    print(f"{numUser} x {countTable} = {numUser*countTable}")

    countTable += 1

    
print("Finaliza bucle while.")
