
"""
Variables, concatenación, interpolación y castear
"""

# Variables
text = "Master en python"
age = "Edad: "
num = 26
name = "Anthony"
lastname = "Tamayo Ortega"
web = "anthonyjobs.co"

print(text)
# Concatenación, interpolación y castear de entero a cadena de texto
print(f"{age} "+str(num)+" años")

# Otra forma de concatenar
print("Hola me llamo {} {} y mi web es: {}".format(name,lastname,web))

#Types
nada = None
cadena = "Soy Anthony Tamayo Ortega Ingeniero Multimedia"
entero = 99
flotante = 4.5
booleano = False
lista = [10, 20, 30, 40, 50, 60, 70]
tupla = ('master', 'en', 'python')
diccionario = {
    "name": "Anthony",
    "lastname": "Tamayo",
    "course": "Master in python"
}
rango = range(9)
dato_byte = b"Probando"

# imprimir variable
print(cadena)
# mostrar tipo de dato
print(type(cadena))

#variable
print(entero)
#tipo de dato
print(type(entero))

#variable
print(flotante)
#tipo de dato
print(type(flotante))

#variable
print(booleano)
#tipo de dato
print(type(booleano))

#variable
print(lista)
#tipo de dato
print(type(lista))

#variable
print(tupla)
#tipo de dato
print(type(tupla))

#variable
print(diccionario)
#tipo de dato
print(type(diccionario))

#variable
print(rango)
#tipo de dato
print(type(rango))

#variable
print(dato_byte)
#tipo de dato
print(type(dato_byte))


numerito = 776
print("Castear una variable")
print(numerito)
print(type(numerito))

#castear a string
numerito = str(numerito)
print(numerito)
print(type(numerito))

#castear a entero
numerito = int(numerito)
print(numerito)
print(type(numerito))

#castear a float
numerito = float(numerito)
print(numerito)
print(type(numerito))
