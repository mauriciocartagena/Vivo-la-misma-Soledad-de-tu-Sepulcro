# Coloca el código de tu juego en este archivo.


# Declara los personajes usados en el juego como en el ejemplo:




define e = Character("Eileen")
define narrator = nvl_narrator

# El juego comienza aquí.


label start:
    
    image police = './images/Historia/Policias.png'
    image drogas = './images/Historia/Drogas.png'

    scene drogas #ESTE ES NOMBRE DE LA IMAGEN 4.1 mas claro el de los carteles
    ""
    "{i}{cps=25}Los avisos tuvieron buen efecto publicitario, fueron colocados
    en diferentes lugares paredes, postes, columnas, vidrieras, escaparates,
    e incluso en las puertas de la emisora de la zona y en los carteles
    de la entrada al salón de actos{/cps}{/i}{nw}"
    ""
    scene police  #ESTE ES NOMBRE DE LA IMAGEN 2 el vehiculo
    "{i}{cps=25}También la sociedad de lucha contra las drogas había contratado 3 vehículos
    con parlantes para hacer conocer la población que no llegaba al centro y cuyas actividades
    estaban en la periférica de la ciudad.{/cps}{/i}{nw}"
    ""
    "{i}{cps=25}Tenia que darse una importancia publicitaria de gran envergadura y pensaba
    que nada se debía escatimar para enfrentar y erradicar de una vez por todas ese mal
    que hacía tanto daño a la sociedad, a la juventud especialmente.{/cps}{/i}"

    nvl clear

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # show eileen happy

    # Presenta las líneas del diálogo.

    # e "Has creado un nuevo juego Ren'Py."

    # e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    # return
