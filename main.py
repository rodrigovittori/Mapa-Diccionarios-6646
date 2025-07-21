# [M5.L1] - Actividad #4: "Transición"

# Implementamos desplazamiento entre habitaciones
# Agregamos condición para terminar el bucle principal

"""
Paso 1) Pedir habitación destino con input()

Paso 2) Verificar que la opción sea válida
        > Si es válida, nos movemos a esa habitación
        > SINO, mostramos un mensaje de error
            > importamos sleep para agregar pausas
            
Paso 3) Agregar condición para que cuando lleguemos a la Salida finalice el Bucle Principal
"""

from time import sleep # Para pausas dramáticas

mapa = {
        # ACTUALMENTE mapa es un diccionario donde cada clave 
        # es asociada a una lista de habitaciones a las que podemos
        # acceder desde ella: 
        
        #       CLAVE       :               VALOR
        # Habitación actual : Lista de habitaciones accesibles
        'Spawn'             : ['1', '2'],
        '1'                 : ['Spawn', '3', '4'],
        '2'                 : ['Spawn', '4'],
        '3'                 : ['1'] , #items
        '4'                 : ['1', '2', 'Boss'],
        'Boss'              : ['4', 'Salida'],
        'Salida'            : ['Boss']
        }

####################################################################
# DECLARACIÓN DE VARIABLES

# Paso 1) Seteamos habitación inicial ("Spawn")
habitacion_actual = "Spawn"

####################################################################
# BUCLE PRINCIPAL DE JUEGO:

while (True): # To-do: Agregar condición para salir del bucle
    # Mostramos habitación actual: 
    print("\n===================================")
    print(" Te encuentras en la habitación:", habitacion_actual)

    # Mostramos habitaciones disponibles/accesibles:
    print("\n Puedes ir a: ")
    for habitacion_contigua in mapa[habitacion_actual]:
        print("> ", habitacion_contigua)

    ########################################################################
    # SOLICITAR HABITACIÓN DESTINO:
    habitacion_destino = input("\n ¿A que habitacion iras ahora?: ")

    if (habitacion_destino not in mapa[habitacion_actual]):
        # Si la habitación elegida por el usuario NO está en la lista asignada a mi clave actual...
        print("¡No puedes hacer eso!, \"", habitacion_destino, "\" NO es accesible desde aquí.")
        sleep(2)
        continue

    # Condición para "terminar" el juego:
    elif (habitacion_destino == "Salida"):
        habitacion_actual = "Salida"
        print("¡Eres libre!")
        sleep(2)
        break

    else:
        # Si la habitacion ES válida y NO es la salida: cambiamos de habitación
        habitacion_actual = habitacion_destino

####################################################################
# FIN DE BUCLE PRINCIPAL

print("\n===================================")
print("\n > FIN DEL JUEGO <")