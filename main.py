# [M5.L1] - Actividad #2: "Habitaciones"

# Creamos diccionario que representa el mapa a recorrer

# NOTA: La actividad Nº 1 no se incluye ya que fue sólo una demo

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