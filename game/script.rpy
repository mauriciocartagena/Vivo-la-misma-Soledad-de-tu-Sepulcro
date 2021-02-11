# Coloca el código de tu juego en este archivo.


# Declara los personajes usados en el juego como en el ejemplo:




define j = Character("Juan Carlos", color="cc0033")
define a = Character("Aime")
define p = Character("Presentadora", color="ff9933")
define narrator = nvl_narrator

# El juego comienza aquí.


label start:

    scene drogas
    with dissolve
    "{nw}"
    "{nw}"
    "{i}{cps=25}Los avisos tuvieron buen efecto publicitario, fueron colocados
    en diferentes lugares paredes, postes, columnas, vidrieras, escaparates,
    e incluso en las puertas de la emisora de la zona y en los carteles
    de la entrada al salón de actos{/cps}{/i}{nw}"
    ""
    hide drogas
    show policias
    with dissolve
    nvl clear
    "{nw}"
    "{i}{cps=25}También la sociedad de lucha contra las drogas había contratado 3 vehículos
    con parlantes para hacer conocer la población que no llegaba al centro y cuyas actividades
    estaban en la periférica de la ciudad.{/cps}{/i}{nw}"
    "{nw}"
    "{i}{cps=25}Tenia que darse una importancia publicitaria de gran envergadura y pensaba
    que nada se debía escatimar para enfrentar y erradicar de una vez por todas ese mal
    que hacía tanto daño a la sociedad, a la juventud especialmente.{/cps}{/i}{nw}"
    ""

    nvl clear


    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # show eileen happy

    # Presenta las líneas del diálogo.
    j "Estas Lista ¿Como te sientes?"
    a "Bastante Nerviosa"
    j "Eso es Normal. Es la primera vez en el escenario,
    hasta los grandes oradores se debieron sentir en su debut"
    a "No paro de sudar de las manos y de temblar"
    j "Calma, todos esos síntomas ya pasaran una vez que estés en el escenario,
    tienes una gran fuerza de voluntad y lograras desenvolverte tranquilamente"
    a "Espero no decaer y llorar en el acto"
    j "Ya lloraste bastante, todo lo malo ya paso"
    j "Ahora es momento levantarse y comenzar esta lucha con las drogas,
    y seas la encargada de dar a conocer los daños que hace a las personas,
    sobre todo a nuestros jóvenes"
    j "Confío en ti, se que lo lograras pese al dificultades que te enfrentes"
    a "Gracias Juan, eres un gran amigo"
    "{nw}"
    "{nw}"
    "{vspace=100} {space=100}En ese momento se dan el abrazo"
    j "Te están llamando
    Suerte, se que lo haras bien, te lo aseguro"
    a "(Tengo suerte de tener a Juan como amigo)"

    scene presentadora

    hide policias
    show presentadora
    with dissolve
    
    p "Muy buenos días y muchas gracias por venir el día de hoy"
    p "Bueno, a todos ustedes querido público, daremos a conocer los grandes problemas
    que trae las drogas y como poder enfrentarlos"
    p "en cada parte de la sociedad, para después tomar conciencia y superarlo ya sea
    en la familia, escuelas o en sus trabajos"
    p "Esta charla de hoy, será parte de nuestra oradora, la cual tuvo que ver como
    el consumo excesivo de dicho mal destruía a su hijo Oscar llevándolo a su muerte"
    p "Oscar un buen joven, podría haber sido el hijo de cualquiera, no importa si eres
    millonario o pobre, la religión que tengas o el color de piel que tengas"
    p "si caes a la merced de la droga caerás hasta el fondo"

    # e "Has creado un nuevo juego Ren'Py."

    # e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    # return
