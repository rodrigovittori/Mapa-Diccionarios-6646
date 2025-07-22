# [M5.L1] - Actividad #5: "Llave"

""" Objetivo: Implementar una nueva condición de victoria:
              el jugador DEBE encontrar la llave para poder activar la Salida

Pasos:

1º) Modificar nuestro diccionario para que cada clave se asocie a un DICCIONARIO (no listas)
    > Cada habitación ahora será un diccionario con DOS CLAVES:
                                                                * Lista de Habitaciones Accesibles
                                                                * Lista de Ítems presentes en la habitación actual

2º) Modificar condición para terminar el bucle principal: 
                                                         A) el jugador DEBE haber derrotado al Boss*
                                                         B) el jugador DEBE estar en "Salida"

                                                         * Nota: Para derrotar al Boss deberemos encontrar un ítem
                                                         
    > crearemos una variable que represente el ítem necesario para salir
    > crearemos un "inventario" (lista) para el jugador
    > finalmente cuando el jugador desee acceder a la Salida deberá poseer el ítem requerido
    
    NOTA: Por cuestiones de dinámica de clase cambiaremos las condiciones para que el ítem "derrote" a nuestro "Boss"

3º) Modificar sistema de transición entre habitaciones
4º) Implementar sistema de recolección de ítems
5º) Modificar sistema de listado de habitaciones contiguas / accesibles
"""

from time import sleep # Para pausas dramáticas

mapa = {
        # 1ª CLAVE (mapa) :    VALOR (otro diccionario)
        #                       2º diccionario (cada habitacion es un diccionario con sus propias listas)
        #                       lista_habitaciones, lista_items, (pueden agregar: lista_trampas y/o lista_enemigos)
        'Spawn'           : { 'lista_habitaciones' : ['1', '2'], 'lista_items' : [] },
        '1'               : { 'lista_habitaciones' : ['Spawn', '3', '4'], 'lista_items' : ["Hacha oxidada"] },
        '2'               : { 'lista_habitaciones' : ['Spawn', '4'], 'lista_items' : ["Chocolate"] },
        '3'               : { 'lista_habitaciones' : ['1'], 'lista_items' : [] },        # <<--- AGREGAR ITEM NECESARIO A ESTA SALA
        '4'               : { 'lista_habitaciones' : ['1', '2', 'Boss'], 'lista_items' : ["Replica"] },
        'Boss'            : { 'lista_habitaciones' : ['4', 'Salida'], 'lista_items' : [] },
        'Salida'          : { 'lista_habitaciones' : ['Boss'], 'lista_items' : [] }
        }

####################################################################
# DECLARACIÓN DE VARIABLES

# Paso 1) Seteamos habitación inicial ("Spawn")
habitacion_actual = "Spawn"

# Paso 2) Definir el item necesario para poder ganar el juego:
item_requerido = "Pollito KFC" # Necesitaremos un "Arma Legendaria" para derrotar al Boss

# Vamos a colocarlo en la habitación '3':
mapa['3']["lista_items"].append(item_requerido)

# Ya que tendremos que registrar ítems no hay motivo para no crear un inventario para nuestro PJ
inventario_personaje = []

# Agreguemos ahora una variable que registre si hemos obtenido el ítem requerido:
tiene_item_requerido = False

# Agreguemos también una segunda condición para saber si hemos derrotado al boss:
boss_derrotado = False

nombre_boss = "Mr. DiplomongUs"

####################################################################
# BUCLE PRINCIPAL DE JUEGO:

while (not (boss_derrotado and (habitacion_actual == "Salida"))): # To-do: Agregar condición para salir del bucle

    ################################################################################################################
    # >> INVENTARIO:

    # Verificamos si nuestro personaje tiene (o no) el ítem requerido:
    tiene_item_requerido = (item_requerido in inventario_personaje)

    # Mostramos inventario
    if (len(inventario_personaje) > 0): # Si tenemos algún ítem:
        print("Inventario: ", inventario_personaje)

    ################################################################################################################
    
    # Mostramos habitación actual: 
    print("\n===================================")
    print(" Te encuentras en la habitación:", habitacion_actual)

    # Mostramos habitaciones disponibles/accesibles:
    print("\n Puedes ir a: ")
    for habitacion_contigua in mapa[habitacion_actual]["lista_habitaciones"]:
        print("> ", habitacion_contigua)

    ########################################################################
    # SOLICITAR HABITACIÓN DESTINO:
    habitacion_destino = input("\n ¿A que habitacion iras ahora?: ")

    if (habitacion_destino not in mapa[habitacion_actual]["lista_habitaciones"]):
        # Si la habitación elegida por el usuario NO está en la lista asignada a mi clave actual...
        print("¡No puedes hacer eso!, \"", habitacion_destino, "\" NO es accesible desde aquí.")
        sleep(2)
        continue

    # Condición para "terminar" el juego:
    elif (habitacion_destino == "Salida"):
        if (boss_derrotado):
            print("¡Felicitaciones! Has derrotado al malo malvado y el reino ha sido salvado :D")
            print(" [GOOD ENDING] ")
            print("¡Eres libre!")
            sleep(2)
            break
        else:
            print(" No esperaba ésto: [ENDING NEUTRAL: SALIDA EQUIVOCADA]")

    ########################################################################
    # Condiciones del Boss
    elif ((habitacion_destino == "Boss") and (tiene_item_requerido)):
        print("Armado con valor sabiendo que tienes lo necesario para liberar este mundo de la crueldad de ", nombre_boss, ", entras al Gran Salón.")
        #print("🎟️ *vale por una pelea epica* - *toi cansado jefe*")
        
        for _ in range (3):
            sleep(1)
            print("...")

        print("Un escalofrío recorre tu espalda y te congelas al escuchar una voz estremecedora inquerir:")
        print("> ¿QUIEN OSA ADENTRARSE EN MI GUARIDA? ¿ACASO SE ATREVEN A DESAFIAR EL PODER DE ", nombre_boss, "?" )

        sleep(2)
        print("\n Incapaces de responder nuestros héroes se quedan ahí sosteniendo ", item_requerido)

        sleep(3)
        print(" *con voz amable* > Oh! Mi pollito! Me moría de hambre, perdón es que no recibo muchas visitas ultimamente...")
        print(" *toma la bolsa y te da un puñado de oro*  > Eso debería ser suficiente, AHORA VETE! ")

        inventario_personaje.append("monedas de oro")

        sleep(2)
        print(nombre_boss, " procede a devorar su ", item_requerido)
        print("Lo que él no sabía es que esa deliciosa salsa no era sólo de arándanos... ¡Tenía veneno de medusas!")

        sleep(3)
        print("> AAAAHHHH! Noooooo, MI DEBILIDAD SECRETA! ¿¡ COMO LO SUPISTE?! ")

        sleep(2)
        print(" ** Antes de que nuestros héroes comenten sobre el peligroso viaje en el que se embarcaron para conseguir un vial de veneno de medusas en el reino submarino de Khat-Mazal el malo continua **")
        print("\n RAYOS, TRUENOS, CENTELLAS, ¡ARÁNDANOS! MI DEBILIDAD ZOI ALERGICO DESDE PEQUEÑO BUAAAAH")
        
        boss_derrotado = True
        habitacion_actual = "Salida"
        sleep(4)
        continue

    elif ((habitacion_destino == "Boss") and (not tiene_item_requerido)):
        print("La presencia del malo malvado es tan maléficamente malvada que tus piernas se vuelven blandas como malvaviscos y no puedes obligarte a entrar.")
        print("AÚN NO ESTAS LISTO, NECESITAS, ", item_requerido, ", ENCUÉNTRALO, ¡RÁPIDO!")
        habitacion_actual = '4'
        sleep(4)

    else:
        # Si la habitacion ES válida y NO es la salida: cambiamos de habitación
        habitacion_actual = habitacion_destino

    ################################################################################################################
    # RECOLECCIÓN DE ÍTEMS:

    """
    Paso 1: Ver si hay items
    Paso 2: Ver si es el item requerido, de ser así mostrar mensaje epicardo bro
    Paso 3: Agregar el item al inventario del PJ (sin importar si es el item requerido o no)
    Paso 4: Eliminar el ítem del mapa (para evitar ítems infinitos)
    """

    if ( len(mapa[habitacion_actual]["lista_items"]) > 0 ):          # Si hay items en esta habitación:
        for item in mapa[habitacion_actual]["lista_items"]:          # iteramos sobre los items...

            ########################################################################
            # MENSAJES DE ÍTEMS:
            
            if item == item_requerido:
                print("¡FELICIDADES! Has conseguido el ítem requerido: ", item_requerido)
                print("Toma este vale por un mensaje con más epicidad: 🎟️")
                sleep(3)

            elif item == "Chocolate":
                print("\n\nRevisando la habitación encuentras un ladrillo suelto en la pared de piedra...")
                sleep(3)
                print("Detrás de él, un alijo escondido con joyas y otras cosas que simplemente dejas a un lado...")
                sleep(3)
                print("Sin embargo, en un delicado envoltorio encuentras una ración extraña.")
                sleep(2)
                print("\n Hesitante, lo muerdes e inmediatamente un DELICIOSO sabor invade tu boca.")
                sleep(2)
                print("Su textura aterciopelada derritiéndose en tu lengüa,\n",
                      "ese comfort cálido que te recuerda las mañanas de tu infancia,\n",
                      "bocado a bocado sientes como este delicioso ítem restaura tus fuerzas.")
                sleep(10)
                print("Con mucho esfuerzo te recuerdas la importancia de tu misión y el peligro que te rodea...")
                sleep(3)
                print("Decides guardar el resto para más tarde. \n\n")
                sleep(2)

            elif item == "Replica":

                print("\n\nEn una estantería encuentras una pequeña caja olvidada.")
                sleep(3)
                print("Tras un breve sobresalto que te genera una araña que había hecho",
                      "de esa caja su hogar al levantar la caja sientes que hay algo dentro de ella.")
                sleep(5)
                print("Encuentras una increíblemente detallada réplica de madera de un revólver.")
                sleep(3)
                print("Te tomas unos minutos para revisar los intrincados detalles labrados...")
                sleep(3)
                print("Aunque sólo se trate de una réplica de madera, comprendes que dentro de ella hay un GRAN poder.")
                sleep(5)
                print("Decides llevarla contigo, aunque sea para tranquilizar tus nervios. \n\n")
                sleep(2)
            
            inventario_personaje.append(item)                        # Agregamos el ítem al inventario del PJ
            print("Has recibido el ítem: ", item)
            mapa[habitacion_actual]["lista_items"].remove(item)      # Eliminamos el item del mapa

####################################################################################################################

####################################################################
# FIN DE BUCLE PRINCIPAL

print("\n===================================")
print("\n > FIN DEL JUEGO <")