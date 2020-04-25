
"""
Variables, concatenación, interpolación y castear
"""

# Variables
text = "Master en python"
age = "Edad: "
num = 26
name = "Anthony"
lastname = "Tamayo Ortega"
web = ""

print(text)
# Concatenación, interpolación y castear de entero a cadena de texto
print(f"{age} "+str(num)+" años")

name = "Anthony"
lastname = "Tamayo Ortega"
web = "anthonyjobs.co"

# Otra forma de concatenar
print("Hola me llamo {} {} y mi web es: {}".format(name,lastname,web))
