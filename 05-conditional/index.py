
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

# Ejemplo 3
print("############ Ejemplo 3 ###############")

day = int(input("Introduce el numero del dia de la semana: "))

if day == 1:
   print("Es lunes")
elif day == 2:
   print("Es martes")
elif day == 3:
   print("Es miercoles")
elif day == 4:
   print("Es jueves")
elif day == 5:
   print("Es viernes")
else:
   print("Es fin de semana")

# Ejemplo 4
print("############### Ejemplo 4 ###############")

edadMinima = 18
edadMaxima = 65
edadOficial = int(input("¿Cual es tu edad?: "))

if edadOficial >= 18 and edadOficial <= 65:
   print("Esta en edad para trabajar !!")
else:
   print("No esta en edad para trabajar.")

"""

Operadores logicos

and Y
or  O
!   Negacion
not NO

"""

