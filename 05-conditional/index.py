
"""
Conditional IF
"""
print("> Condition IF")

# Ejemplo 1
print("########### EJEMPLO 1 ###############")

color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
   print("Genial")
   print("Adivinaste, mi color es rojo")

else:
    print("El color es incorrecto")

# Ejemplo 2
print("############ Ejemplo 2 ##############")

year = int(input("¿En que año estamos?: "))

if year < 2021:
   print("El año es anterior al 2021")
else:
   print("El año es posterior al 2021")
