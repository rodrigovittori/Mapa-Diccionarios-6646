# [M5.L1] - Actividad #3: "Bucle Principal"

# Creamos bucle principal
# Nota: Por ahora sólo mostraremos nuestra habitación actual
#       y aquellas a las que podemos acceder desde "aquí"

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

    # Agregamos un input() para evitar un bucle infinito...
    print("En la próxima tarea pediremos al jugador que elija hacia que habitación avanzar...")
    input("Presione [Enter] para continuar...")