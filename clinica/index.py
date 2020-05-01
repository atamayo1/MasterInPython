
mensajeInicio = '***** SOFTWARE DE LA CLINICA BIENVENIDOS *****'
opcionesClínica = [
    '1. Conocer cupo de un piso',
    '2. Registrar un paciente',
    '3. Retirar un paciente',
    '4. Buscar un paciente',
    '5. Mover un paciente de piso',
    '6. Mostrar ocupación de la clínica',
    '0. SALIR',
]
totalPisos = 5
totalHabitacionPorPiso = 4
totalHabitaciones = totalHabitacionPorPiso * totalPisos
pacientes = []
pisosOcupados = []
contadorPacientePiso1 = []
contadorPacientePiso2 = []
contadorPacientePiso3 = []
contadorPacientePiso4 = []
contadorPacientePiso5 = []
tiposDePisos = [
    '1. Pacientes cuidados intensivos',
    '2. Pacientes cuidados intermedios',
    '3. Pacientes de urgencias',
    '4. Pacientes en recuperación',
    '5. Pacientes en recuperación'
]

# funcion que muestra las listas
def mostrarLista(lista):
    resultado = ""

    for mensaje in lista:
        resultado += mensaje
        resultado += "\n"

    return resultado

"""
1.	Cupo de un piso: Desarrolle una función o procedimiento que, 
    según un piso dado por el usuario, indique cuántas habitaciones 
    disponibles (no ocupadas) quedan en ese piso.
"""

def cupoDelPiso():
    resultado = ""
    piso = int(input("Ingrese el piso a consultar: "))

    if len(pisosOcupados) == totalPisos:
        resultado = f"Las {totalHabitaciones} habitaciones que dispone la clinica estan llenas"
    else:
            if piso == 1:
                resultado += str(contadorPacientePiso1)
                print(f"El piso {piso} tiene ocupado {len(contadorPacientePiso1)} habitaciones de {totalHabitacionPorPiso} habitaciones disponibles")
                if len(contadorPacientePiso1) == totalHabitacionPorPiso:
                    for pisoOcupado in pisosOcupados:
                        if(pisoOcupado == piso):
                            print(f"Piso {piso} ocupado")

            if piso == 2:
                resultado += str(contadorPacientePiso2)
                print(f"El piso {piso} tiene ocupado {len(contadorPacientePiso2)} habitaciones de {totalHabitacionPorPiso} habitaciones disponibles")
                if len(contadorPacientePiso2) == totalHabitacionPorPiso:
                    for pisoOcupado in pisosOcupados:
                        if(pisoOcupado == piso):
                            print(f"Piso {piso} ocupado")

            if piso == 3:
                resultado += str(contadorPacientePiso3)
                print(f"El piso {piso} tiene ocupado {len(contadorPacientePiso3)} habitaciones de {totalHabitacionPorPiso} habitaciones disponibles")
                if len(contadorPacientePiso3) == totalHabitacionPorPiso:
                    for pisoOcupado in pisosOcupados:
                        if(pisoOcupado == piso):
                            print(f"Piso {piso} ocupado")

            if piso == 4:
                resultado += str(contadorPacientePiso4)
                print(f"El piso {piso} tiene ocupado {len(contadorPacientePiso4)} habitaciones de {totalHabitacionPorPiso} habitaciones disponibles")
                if len(contadorPacientePiso4) == totalHabitacionPorPiso:
                    for pisoOcupado in pisosOcupados:
                        if(pisoOcupado == piso):
                            print(f"Piso {piso} ocupado")

            if piso == 5:
                resultado += str(contadorPacientePiso5)
                print(f"El piso {piso} tiene ocupado {len(contadorPacientePiso5)} habitaciones de {totalHabitacionPorPiso} habitaciones disponibles")
                if len(contadorPacientePiso5) == totalHabitacionPorPiso:
                    for pisoOcupado in pisosOcupados:
                        if(pisoOcupado == piso):
                            print(f"Piso {piso} ocupado")

    return resultado

"""
2.	Registrar un paciente: Desarrolle una función o procedimiento que 
    le ingresa como parámetro un paciente y un piso, de manera que el 
    paciente debe quedar registrado dentro de la clínica en el respectivo 
    piso (siempre y cuando haya cupo en el piso). Es recomendable que elabore 
    una función para crear al paciente, de manera que se le pidan al usuario 
    los datos del paciente (cédula, nombre, enfermedad principal, edad, sexo) 
    y retorne el paciente creado para luego ser registrado en la clínica.
"""

def registroPaciente():
    resultado = ""

    if len(pacientes) > 0:
        print(str(pacientes))

    paciente = []
    cedula = input("Ingrese cédula del paciente: ")
    paciente.append(cedula)
    nombre = input("Ingrese nombre del paciente: ")
    paciente.append(nombre)
    enfermedadPrincipal = input("Ingrese enfermedad principal del paciente: ")
    paciente.append(enfermedadPrincipal)
    edad = input("Ingrese edad del paciente: ")
    paciente.append(edad)
    sexo = input("Ingrese el sexo del paciente 'M' para masculino y 'F' para femenino: ")
    paciente.append(sexo)
    print("\n")
    print("Tipos de pacientes")
    print(mostrarLista(tiposDePisos))
    piso = int(input("Ingrese el piso del paciente del 1 al 5: "))

    if piso > 0 and piso < 6:

        if piso == 1:
            contadorPacientePiso1.append(1)
            paciente.append(piso)
            pacientes.append(paciente)
            resultado += str(paciente)+" "+str(contadorPacientePiso1)
            if len(contadorPacientePiso1) == 4:
                pisosOcupados.append(piso)
                print(str(pisosOcupados))
                for pisoOcupado in pisosOcupados:
                    if(pisoOcupado == piso):
                        print(f"Piso {piso} ocupado")

        if piso == 2:
            contadorPacientePiso2.append(1)
            paciente.append(piso)
            pacientes.append(paciente)
            resultado += str(paciente)+" "+str(contadorPacientePiso2)
            if len(contadorPacientePiso2) == 4:
                pisosOcupados.append(piso)
                print(str(pisosOcupados))
                for pisoOcupado in pisosOcupados:
                    if(pisoOcupado == piso):
                        print(f"Piso {piso} ocupado")

        if piso == 3:
            contadorPacientePiso3.append(1)
            paciente.append(piso)
            pacientes.append(paciente)
            resultado += str(paciente)+" "+str(contadorPacientePiso3)
            if len(contadorPacientePiso3) == 4:
                pisosOcupados.append(piso)
                print(str(pisosOcupados))
                for pisoOcupado in pisosOcupados:
                    if(pisoOcupado == piso):
                        print(f"Piso {piso} ocupado")

        if piso == 4:
            contadorPacientePiso4.append(1)
            paciente.append(piso)
            pacientes.append(paciente)
            resultado += str(paciente)+" "+str(contadorPacientePiso4)
            if len(contadorPacientePiso4) == 4:
                pisosOcupados.append(piso)
                print(str(pisosOcupados))
                for pisoOcupado in pisosOcupados:
                    if(pisoOcupado == piso):
                        print(f"Piso {piso} ocupado")

        if piso == 5:
            contadorPacientePiso5.append(1)
            paciente.append(piso)
            pacientes.append(paciente)
            resultado += str(paciente)+" "+str(contadorPacientePiso5)
            if len(contadorPacientePiso5) == 4:
                pisosOcupados.append(piso)
                print(str(pisosOcupados))
                for pisoOcupado in pisosOcupados:
                    if(pisoOcupado == piso):
                        print(f"Piso {piso} ocupado")

    else:
        resultado += "Piso invalido"
        print(iniciarSoftware())

    if resultado:
        print("Se ha registrado correctamente")

    return resultado


"""
3.	Retirar un paciente: Desarrolle una función o procedimiento que, 
    dada una cédula de un paciente, lo retire de la habitación en que 
    se encuentra y por ende también de la clínica.
"""

def retirarPaciente():
    resultado = ""
    cedula = input("Ingrese cédula del paciente a retirar: ")
    return resultado

"""
4.	Buscar un paciente: Desarrolle una función o procedimiento que dada
    una cédula indique si el paciente se encuentra en la clínica, en qué 
    piso y en qué habitación (las habitaciones son la 1, 2, 3 y 4). Por 
    ejemplo (“El paciente se encuentra registrado en el segundo piso, 
    habitación 2”).
"""

def buscarPaciente():
    resultado = ""
    cedula = input("Ingrese la cédula a consultar: ")
    return resultado

"""
5.	Mover un paciente de piso: Desarrolle una función o procedimiento que 
    recibe como parámetro una cédula y un piso, de manera que el paciente 
    sea retirado del piso en que está y quede registrado en el nuevo piso 
    (siempre y cuando haya cupo en el piso).
"""

def moverPaciente():
    resultado = ""
    cedula = input("Ingrese la cédula del paciente que desea mover: ")
    piso = input("¿Cual es el piso al que va ir el paciente? ")
    return resultado

"""
6.	Mostrar ocupación de clínica: realice una función o procedimiento que 
    muestre gráficamente (en forma de matriz, por ejemplo) qué habitaciones 
    se encuentran ocupadas (con los datos del paciente) y qué habitaciones 
    se encuentran disponibles (marcadas con un O), abajo hay una imagen 
    de ejemplo donde se observan 2 habitaciones ocupadas, una en el segundo 
    piso, y otra en el quinto piso, el resto de las habitaciones se encuentras 
    disponibles.
"""

def mostrarOcupaciones():
    resultado = ""
    return resultado

"""
7.	Salir: dé al usuario una opción para salir del menú, recuerde que hasta que 
    el usuario no elija esta opción el programa no debería terminar.
"""

def salir():
    resultado = "Has salido correctamente del software"
    return resultado

"""
Finalizan las funciones
"""

def iniciarSoftware():
    print("\n")
    print(mensajeInicio)
    print(mostrarLista(opcionesClínica))
    opcionSeleccionada = int(input("¿Coloque el número de la opción que desea seleccionar del 0 al 6? "))

    if opcionSeleccionada >= 0 and opcionSeleccionada < 7:

        if opcionSeleccionada == 0:
            print(salir())

        if opcionSeleccionada == 1:
            print(cupoDelPiso())
            continuar = input("Desea realizar otra operacion 'S' para si y 'N' para no: ")

            if continuar == "S":
                print(iniciarSoftware())
            else:
                print("Gracias por su visita vuelva pronto")

        if opcionSeleccionada == 2:
            print(registroPaciente())
            continuar = input("Desea realizar otra operacion 'S' para si y 'N' para no: ")

            if continuar == "S":
                print(iniciarSoftware())
            else:
                print("Gracias por su visita vuelva pronto")

        if opcionSeleccionada == 3:
            print(retirarPaciente())
            continuar = input("Desea realizar otra operacion 'S' para si y 'N' para no: ")

            if continuar == "S":
                print(iniciarSoftware())
            else:
                print("Gracias por su visita vuelva pronto")

        if opcionSeleccionada == 4:
            print(buscarPaciente())
            continuar = input("Desea realizar otra operacion 'S' para si y 'N' para no: ")

            if continuar == "S":
                print(iniciarSoftware())
            else:
                print("Gracias por su visita vuelva pronto")

        if opcionSeleccionada == 5:
            print(moverPaciente())
            continuar = input("Desea realizar otra operacion 'S' para si y 'N' para no: ")

            if continuar == "S":
                print(iniciarSoftware())
            else:
                print("Gracias por su visita vuelva pronto")

        if opcionSeleccionada == 6:
            print(mostrarOcupaciones())
            continuar = input("Desea realizar otra operacion 'S' para si y 'N' para no: ")

            if continuar == "S":
                print(iniciarSoftware())
            else:
                print("Gracias por su visita vuelva pronto")

    else:
        print("Número invalido")


print(iniciarSoftware())


