# Coloca el código de tu juego en este archivo.
image logo = "game_menu.png"
# Declara los personajes usados en el juego:
define circleirisout = ImageDissolve("ilustracion7-4.png", 1.0, 8)
define s = Character("Sara", window_background="gui/textbox.png")
define pm = Character("Mamá", window_background="gui/textbox.png")
define ph = Character("Papá", window_background="gui/textbox.png")

define pg = Character("Padre G.", window_background="gui/textbox.png")

define p = Character("[name]", who_color="#ffffff")
define e = Character("Alumno", who_color="#ffffff")
define g = Character("Gabriela", window_background="gui/textboxRojo.png", who_color="#d40000")
define m = Character("Maestro", window_background="gui/textboxCafe.png", who_color="#ffffff")
define n = Character("Niño", window_background="gui/textboxVerde.png", who_color="#0c6b17")
define ns = Character("Niños", window_background="gui/textboxVerde.png", who_color="#0c6b17")
label splashscreen:
    show game_menu

    with dissolve
    with Pause (4.5)
    hide game_menu
    with dissolve
    #menu:
        #"CONTINUAR.":

        #    jump continuar
#label continuar:
    return
# El juego comienza aquí.


label start:


    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene fondoejm

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show ext
    play music "sound/intro.mp3"



    # Presenta las líneas del diálogo.

    "Desde que nacemos vivimos con miedo"
    "Pero... {w=2}con miedo a que?"
    "Hay muchas razones pero con el tiempo te enteras que ninguna es la
    correcta y en esa búsqueda no nos damos cuenta."
    "En lo que nos estamos convirtiendo."

    scene ventanaejm
    with fade

    "cada mañana parece ser un dia normal"
    "el sol sale, los adultos van al trabajo y los niños a la escuela"
    "Sara siempre se va a su escuela sin sus padres, ya que ellos trabajan mucho
    todo el día y no tienen casi tiempo para ella."
    "aun así parece ser que a Sara eso no le molesta, ya que ella siempre estará
    acompañada por mi y aunque soy alguien callado"
    "acompañare a sara y jugare con ella en todo momento."


    python:
        name = renpy.input(_("agrega aquí el nombre de tu personaje y oprima Enter para continuar"))



    show sara1ejm
    with dissolve

    s "Date prisa se va hacer tarde [name]"
    hide sara1ejm
    show sara2ejm
    with dissolve

    p "Ya voy"
    hide sara2ejm
    show sara3ejm
    with dissolve

    p "No importa lo que pase yo estaré ahí y cada decisión que tome Sara yo la
    apoyare."
    play music "sound/fondo-cole.wav"
    scene colegioejm
    with dissolve


    p "Esa misma mañana en horarios de clase llegó un nuevo estudiante una persona
    muy alegre con un cabello corto y una sonrisa en su rostro"
    p " no le causo ningún problema presentarse en el pizarrón"
    scene ilustracion1
    show gabriela
    with dissolve

    e "Hola!"
    play music "sound/happy-sandbox.wav"
    e "Mucho gusto"

    e "Me llamo Gabriela pero mis amigos me dicen Gabi"
    show ilustracion3
    g "Espero que nos llevemos bien"
    scene ilustracion4
    p "Todos los niños e incluso el maestro quedaron sorprendidos ante tanta
    seguridad"
    scene fondo2
    show ilustracion5
    with dissolve
    p "Sara quedó anonadada por esa alegre presencia"
    hide ilustracion5
    show ilustracion6
    with dissolve
    p "Pero tuvo que voltear su mirada hacia su mesa para no llamar la atención
    de Gabriela"
    scene ilustracion4
    m "Muy bien Gabriela..!"
    m "puedes sentarte al lado de un compañero para así continuar con la clase"

    play music "sound/sad-heaven-piano-3.mp3"

    scene ilustracion7
    show ilustracion71
    with dissolve
    p "En la hora de recreo todos los estudiantes se acercaron a Gabriela
    empujando a Sara y haciendo caer sus cosas"
    p "como si fuera un accidente.."
    p "empezaron a hacerle preguntas a Gabriela"

    p "Sara se quedo muy atras"
    hide ilustracion71
    show ilustracion8
    with dissolve
    p "así que levanto sus cosas y salio del aula."

    p "mientras caminábamos me comentaba sobre lo genial que se ve Gabriela"
    p "Todo iba bien hasta que de repente aparecieron ellos..."
    scene ilustracion10
    show ilustracion101
    with dissolve
    p "los niños al darse cuenta de la presencia de Sara se fueron hacia otro lado
    sin dirigirle la mirada"
    p "Mientras continuamos caminando"
    scene ilustracion11
    show ilustracion111
    with dissolve
    p "De la nada le llego una bolsa de jugo"
    scene ilustracion12
    show ilustracion121
    with dissolve


    p "uno de los niños le había arrojado eso a sara"

    n "DÓNDE ESTÁ TU AMIGO NIÑA RARA!!!..."
    hide ilustracion121
    show ilustracion122
    with dissolve
    p "Sara se agacho tapándose la cabeza"
    p "tenía unas ganas de llorar pero me puse frente a ella"
    p "Sara levantó la mirada y vio en mí una sonrisa"
    p "una sonrisa como la de Gabriela"
    hide ilustracion122
    show ilustracion3
    with dissolve
    show recuerdo
    with dissolve
    p "esa sonrisa de seguridad de que todo va estar bien"
    hide recuerdo
    scene ilustracion12
    show ilustracion123
    with dissolve
    p "sara se levantó y secó sus lágrimas"
    scene ilustracion7
    p "Después del receso todos los estudiantes volvieron a sus respectivas aulas"
    show ilustracion13
    with dissolve
    p "Sara volvió a su mesa y al tomar asiento, gabriela noto que el cabello de
    sara estaba manchado con leche"
    p "se levantó preocupada pero ya había llegado el profesor y comenzó a dar la
    clase"

    scene ilustracion15
    show ilustracion15-1
    p "En la clase se escuchaba murmurar a los alumnos, de una manera burlona"
    show ilustracion15-1
    p "tanto que cada vez se hacia mas fuerte aquellas burlas, hasta que ya era
    más fácil de entender"
    scene ilustracion14
    show ilustracion14-1
    with dissolve
    p "Gabriela parecía perdida y algo atemorizada de las risas de los estudiantes"
    scene ilustracion7
    show ilustracion7-1
    p "cada segundo era más doloroso para sara"
    show ilustracion7-1
    p "se sentía pequeña..."
    show ilustracion7-1
    p "excluida..."
    show ilustracion7-4#fondo negro
    p "sola..."
    p "Este momento es realmente triste."
    p "no entiendo porque se ríen o porque se burlan"
    p "no encuentro gracia en ello"
    p "talvez..."
    p "la humillación no es divertida para quien conoce al humillado"
    scene ilustracion17
    p "El bullicio en el aula se ve interrumpida por el profesor y el silencio
    se hizo presente"
    scene ilustracion18
    p "en estos momentos se podía sentir algo de paz"
    p "en horarios de salida después de aquel momento"
    p "Gabriela se acercó a sara, dirigiéndose hacia nuestro asiento"
    #sara se puso incomoda y nerviosa
    scene ilustracion19
    show ilustracion19-1
    play music "sound/pianoambient.mp3"
    g "hola..!"
    s "..."
    hide ilustracion19-1
    show ilustracion19-2
    with dissolve
    g "¿Cómo te llamas?"
    s "s..s..Sara"
    hide ilustracion19-2
    show ilustracion19-3
    with dissolve
    g "Me llamo gabriela"
    s "eso.. lose.."
    hide ilustracion19-3
    show ilustracion19-4
    with dissolve
    g "lo siento es la costumbre jejeje"
    hide ilustracion19-4
    show ilustracion19-2
    with dissolve
    g "Quería preguntarte porque tienes el cabello manchado"
    s "unos niños.."
    hide ilustracion19-2
    show ilustracion19-5
    with dissolve
    g "mm...?"
    s "no es nada."
    hide ilustracion19-5
    show ilustracion19-6
    with dissolve
    p "Gabriela parecía muy insistente"

    p "Así que se sentó al lado de sara pero en ese
    entonces Sara..."
    scene ilustracion20
    show ilustracion20-1
    show ilustracion20-2
    with dissolve
    s "QUE ESTÁS HACIENDO!!!!"
    p "Gabriela estaba algo asustada por el grito de Sara"
    p "Pero aun asi gabriela respondió"
    g "solo me estoy sentando"
    s "ahí se sienta [name]"
    g "[name]?... pero no hay nadie aqui"
    s "No hay nadie?"
    s "QUÍTATE!!"
    hide ilustracion20-2
    scene ilustracion7
    show ilustracion21
    with dissolve
    p "Sara empujo a gabriela de su asiento y se fue molesta"
    hide ilustracion21
    scene ilustracion22
    show ilustracion22-1
    with dissolve
    p "Gabriela ya en el suelo desconcertada y algo asustada de lo ocurrido, veía
    cómo Sara se alejaba de ella ante la multitud viéndola."
    g "Quien esta niña?"

    hide ilustracion22-1
    scene ilustracion23
    show ilustracion23-1
    with dissolve

    #cap2
    play music "sound/piano-loop-1.wav"
    s "no puedo creer que se haya sentado en tu lugar sin antes preguntarte [name]"
    s "es igual que todos los niños, solo busca burlarse de mí"
    s "pero..."
    hide ilustracion23-1
    show ilustracion23-2
    with dissolve
    s "creo que no debi empujarla de esa manera"
    s "[name] crees que deberia..."
    menu:

        "Pedir disculpas.":

            jump pedir_disculpas

        "Ignorar lo ocurrido.":

            jump ignorar_lo_ocurrido
label pedir_disculpas:
    s "tienes razón [name] cuando llegue al colegio me disculpare con gabriela"
    p "sara se muestra muy confiada espero le vaya bien hoy"
    scene ilustracion7
    show ilustracion24
    show ilustracion24-1

    play music "sound/ambienteascensor.wav"
    p "al momento de llegar al colegio sara se dirige hacia gabriela"
    hide ilustracion24
    with dissolve
    p "pero en el intento Gabriela se dirige hacia otra compañera para hablar"
    s "parece que está ocupada se lo diré en el recreo"
    scene ilustracion10
    show ilustracion25
    p "sara intentó disculparse en el receso"
    p "pero Gabriela se fue a donde sus compañeros dejando a Sara atrás con las
    palabras en la boca"
    s "amm..."
    s "Gabriela..."
    p "gabriela no hacía caso sobre los intentos de comunicarse de Sara"
    p "pero aun asi intento dar lo mejor de ella, para poder disculparse"
    p "aunque.. en ese momento llegan unos compañeros de curso y se acercaron a
    Sara de forma intimidante"
    scene ilustracion26
    show ilustracion26-1

    n "porque no mejor te vas a estudiar con tus amigos"
    n "solo estas incomodando con tus balbuceos"
    s "lo siento yo solo quería..."
    #le llega a sara bolas de papel
    show ilustracion26-2
    hide ilustracion26-1
    with dissolve
    n "VETE NIÑA RARA!!!"
    show ilustracion26-3
    hide ilustracion26-2
    with dissolve
    ns "SI VETE!!"
    scene ilustracion7
    show ilustracion7-1
    with dissolve
    p "sara se fue a su mesa  algo triste y decepcionada"
    s "Nose que estoy haciendo mal"
    s "todos son malos conmigo"
    s "creo que tengo que ser como Gabriela para que no me traten tan mal"
    s "Apenas lleva dos días aquí y ya se lleva bien con todos los compañeros"
    s "será una buena idea o no será necesario"
jump opcion1
label ignorar_lo_ocurrido:
    $ menu_flag = False
    s "no tengo el porqué pedir disculpas ella empezó"
    s "además ya lo debió olvidar no fue tan grave"
    p "Sara está confundida después de lo que pasó"
    p "Es como si lo que hizo no fuera lo correcto"
    hide ilustracion7-1
    show colegioejm
    with dissolve
    play music "sound/fondo-cole.wav"
    p "ya es de mañana Sara se prepara para ir a la escuela"
    p "Al momento de entrar al aula, Sara ve a Gabriela y nota que ella está
    esta tranquila hablando con sus compañeros"
    p "Sara se fue a su asiento, como siempre algo apartada de los demás"
    p "Solo podía ver como Gabriela se llevaba bien con los demás"
    hide colegioejm
    show ilustracion112
    with dissolve
    s "Gabriela siempre está sonriendo y se lleva bien con todos"
    s "Apenas lleva unos días aquí......"
    s "Tal vez debería ser como Gabriela"
    s "Crees que....... ?"
label opcion1:
    menu:


        "No es necesario.":

            jump no_es_necesario
        "Es una buena idea.":

            jump es_una_buena_idea

label es_una_buena_idea:

    s "decidido!.. desde mañana tratare de cambiar y seré igual que Gabriela"
    p "no importa la decisión que tome sara yo la apoyare siempre."
    #al dia siguiente
    scene ilustracion27
    play music "sound/happy-sandbox.wav"
    p "esta mañana Sara se puso pensativa sobre lo que tendría que cambiar para
    agradarle a todos"
    s "Gabriela siempre esta con una sonrisa"
    s "tal vez debería sonreír más"

    p "cuando bajamos para desayunar habia una nota que decía"
    scene ilustracion28
    hide ilustracion27
    "el desayuno está en el microondas"
    scene colegioejm
    show ilustracion29
    with dissolve
    p "en el camino Sara se decia asi misma 'sonríe' "
    s "'Sonrie Sara', 'Sonrie Sara', 'Sonrie Sara'."
    hide ilustracion29
    scene ilustracion30
    show ilustracion30-1
    with dissolve
    p "Cuando entro al aula Sara soltó una sonrisa de oreja a oreja
    aunque se veía muy forzada, Sara intentaba que esto no le molestara"
    p "todos los alumnos se quedaron callados al verla"
    p "como si se vieran incomodados por su sonrisa"
    p "Sara se dirige hacia su asiento mientras todos se hacían a un lado"
    hide ilustracion30-1
    scene ilustracion19
    show ilustracion19-7
    with dissolve
    p "cuando gabriela vio a sara y noto que ella está sonriendo, ella también
    se puso a sonreír"
    hide ilustracion19-7
    show ilustracion19-8
    with dissolve
    p "Al parecer a Gabriela no le incomodaba el hecho que Sara está sonriendo"
    #continuar
    p "llegó el profesor , todos se sentaron y comenzó la clase"
    hide ilustracion19-8
    show ilustracion19-9
    with dissolve
    p "El profesor en medio de la clase voltea, ve a Sara y le pregunta "
    hide ilustracion19-9
    scene ilustracion
    show ilustracion31-1
    with dissolve
    m "Sara?"
    hide ilustracion31-1
    show ilustracion31-2
    with dissolve
    s "Si profesor?"
    hide ilustracion31-2
    show ilustracion31-1
    with dissolve
    m "Que te hace tan gracioso?"
    hide ilustracion31-1
    show ilustracion31-2
    with dissolve
    s "Nada.."
    hide ilustracion31-2
    show ilustracion31-1
    with dissolve
    m "O mi clase te hace reir?"
    hide ilustracion31-1
    show ilustracion31-3
    with dissolve
    s "No profesor"
    hide ilustracion31-3
    show ilustracion31-1
    with dissolve
    m "Entonces es abubrrida mi clase?"
    hide ilustracion31-1
    show ilustracion31-4
    with dissolve
    s "... no es eso profesor"
    hide ilustracion31-4
    show ilustracion31-6
    with dissolve
    m "Quite esa sonrisa y ponga atención"
    hide ilustracion31-6
    show ilustracion31-5
    with dissolve
    s "si profesor.."
    hide ilustracion31-5
    scene ilustracion7
    show ilustracion7-1
    with dissolve

    play music "sound/sad-heaven-piano-3.mp3"
    p "En el receso se podía escuchar la burlas de los compañeros"
    p "Aunque a Gabriela parecía no gustarle aquellas burlas"
    s "El profesor me llamo la atencion, nose si deberia seguir con esta idea"
    menu:
        "Deberias dejarlo.":

            jump deberias_dejarlo1

        "Continuar con la idea.":

            jump continuar_con_la_idea

label continuar_con_la_idea:
    hide ilustracion7-1
    scene fondo2
    show ilustracion32_1
    with dissolve
    s "Tienes razón, no importa si el profesor se molestó
    debo continuar sonriendo."
    p "Sara realmente es alguien fuerte"
    p "no entiendo porque a nadie le cae bien Sara"
    show ilustracion32_2
    with dissolve
    n "Sara!!? porque no quitas esa sonrisa estúpida de tu cara"
    ns "JAJAJAJAJAJA...!!"
    hide ilustracion32_1
    show ilustracion32_3
    with dissolve
    s "Hola"
    p "al niño no parece haberle gustado esa sonrisa"
    hide ilustracion32_3
    show ilustracion32_4
    with dissolve

    n "¡ VAMOS!!, SONRIE!!, niña rara!"
    hide ilustracion32_2
    hide ilustracion32_4
    show ilustracion32_5
    with dissolve
    p "mientras Sara se limpiaba la cara"
    p "El niño tiró sus cosas al suelo y se fue"
    p "Gabriela intento ayudar a sara, pero mientras se acercaba aquel niño le
    dijo..."
    n "si te haces amiga de esa niña rara...
    Serás parte de la burla"
    p "Gabriela se quedó quieta pero... después de un tiempo retrocede"
    scene colegioejm
    hide ilustracion32_5
    show ilustracion32_6
    with dissolve
    p "terminando las clases sara alistó sus cosas
    y decidió irse lo más pronto posible"
    p "pero gabriela nos dio alcance e invitó a sara a comer un helado"
    hide ilustracion32_6
    show ilustracion32_7
    with dissolve
    play music "sound/happy-piano.MP3"
    g "Sara! espera un momento!..."
    hide ilustracion32_7
    show ilustracion32_8
    with dissolve
    g "vamos a comer un helado"
    s "yo... mm..."
    s "si vamos"
    scene ilustracion33-1
    hide ilustracion32_8
    show ilustracion33-2
    with dissolve
    p "en el camino Gabriela noto la triste cara de Sara"
    g "no debes dejar que te afecte"
    s "ya estoy acostumbrada"
    s "además [name] está conmigo"
    g "quien es [name]"
    s "[name] es mi mejor amigo"
    g "mm... no lo conozco"
    s "está aquí conmigo"
    hide ilustracion33-2
    show ilustracion33-3
    with dissolve
    s "el es [name]"
    p "Gabriela parecía algo confundida pero se quedo y me saludo"
    hide ilustracion33-3
    show ilustracion33-4
    with dissolve
    g "hola [name] me alegro de que acompañes a sara en cada momento"
    g "espero que siempre estes con ella"
    p "Sara no se lo podía creer"
    p "pero en ese momento"
    p "llegaron los padres de gabriela y se fue con ellos"
    p "no sin antes despedirse de nosotros"
    scene ilustracion34
    hide ilustracion33-4
    with dissolve
    g "Adiós Sara cuidate"
    g "Adiós [name] cuida a Sara"

    play music "sound/gregorquendel.wav"
    show texto1
    with dissolve
    with Pause (3.5)
    hide texto1
    #with dissolve
    hide ilustracion34
    show ilustracion35
    with dissolve
    s "ella... te saludo..."
    p "Sara se puso a soltar lágrimas, intentaba contenerse pero..."
    s "no debo llorar"
    s "se supone que debo sonreir pero..."
    hide ilustracion35
    show ilustracion36
    with dissolve
    s "no puedo evitarlo.. esto me pone feliz."
    #cap3
    hide ilustracion36
    show ilustracion27
    with dissolve
    p "ya es de mañana y sara parece estar más animada"
    p "creo hoy será un buen dia."

    play music "sound/vabsounds.mp3"
    scene ilustracion23
    hide ilustracion27
    show ilustracion23-3
    with dissolve
    s "me acabo de dar cuenta que sonreír cada rato no es bueno"
    s "solo tengo que sonreír cuando realmente me sienta feliz"
    p "Sara tiene más confianza en sí misma, eso me tranquiliza"
    hide ilustracion23-3
    show ilustracion18
    with dissolve
    p "hoy toca educación física"
    p "los compañeros se alistan para salir a la cancha"
    p "Sara se acerca a Gabriela y empieza a hablarle"
    p "los demás niños observan a Sara y gabriela algo incómoda intenta evitar
    una conversación con ella"
    hide ilustracion18
    show ilustracion9
    with dissolve
    s "Hola Gabriela!"
    g "hola emm... tengo que alistarme"
    scene ilustracion9-1
    hide ilustracion9
    show ilustracion9-2
    with dissolve
    m "Para el ejercicio de hoy trabajaremos con un compañero para que nos apoye"
    hide ilustracion9-2
    show ilustracion9-3
    with dissolve
    s "Gabr...."
    hide ilustracion9-3
    show ilustracion9-4
    with dissolve
    s "No!.. si  trabajo con Gabriela are a un lado a [name] "
    s "no puedo hacerle eso"
    p "Sara se encuentra pensativa de lo que va hacer"
    s "mm.. bueno."
    p "Parece ser que ya tomó una decisión."
    hide ilustracion9-4
    with dissolve
    s "Gabriela!!!"
    s "se dirige hacia Gabriela de una forma muy alegre y confiada pero.."
    hide ilustracion9-4
    show ilustracion9-5
    with dissolve
    g "No puedo."
    g "ya tengo compañero en verdad lo siento"
    p "se podía sentir las miradas y burlas hacia Sara, incluso se podía observar
    lo distante que se ve Sara hacia sus compañeros"
    p "cada segundo parecía estar más lejos"
    hide ilustracion9-5
    show ilustracion9-6
    with dissolve
    p "en el transcurso del tiempo nos quedamos solos realizando los ejercicios"
    p "Sara me preguntó"
    s "debería intentar otra vez hablar con Gabriela..?"
    menu:

        "Es una buena idea.":

            jump es_una_buena_idea1

        "Sigamos con la clase.":

            jump sigamos_con_la_clase

label sigamos_con_la_clase:
    s "si.. mejor continuemos"
    s "además está cerca de los niños que me molestan"
    hide ilustracion9-6
    show ilustracion32_7
    with dissolve
    p "terminado la clase de Educacion Fisica Sara se alista para la salida y
    en la puerta de la entrada se encontraba Gabriela esperandonos"
    g "perdón por no poder tu compañera en la clase"
    s "no te preocupes.. jeje"
    hide ilustracion32_7
    show ilustracion32_8
    with dissolve
    g "vamos por helado?"
    s "claro vamos!!"
    scene ilustracion
    hide ilustracion32_8
    show ilustracion33-2
    with dissolve
    p "continuaron hablando en el camino de muchas cosas como programas de tv o
    de dibujos nunca vi a Sara tan segura de sí misma"
    g "porque te molestan tanto?"
    s "me molestan por [name]"
    g "que tienen con [name]"
    s "me molestan por tener un amigo que ellos no pueden ver"
    g "bueno.. yo pienso que tener un amigo es algo muy bueno"
    g "te ayuda en los malos momentos"
    g "te apoya en tus decisiones y sobre todo nunca te haría sentir sola"
    g "pero... no es el único"
    g "¡¡¡ PUEDES HACER MUCHOS AMIGOS!!!"
    hide ilustracion33-2
    show ilustracion9-7
    with dissolve
    p "sara vio una luz"
    p "se reflejaba en su mirada aquella felicidad que había perdido"
    s "Aun puedo hacer muchos amigos"
    s "se que puedo."
    hide ilustracion7-7
    scene ilustracion23
    show ilustracion23-4
    with dissolve
    #en la mañana
    play music "sound/fondo-cole.wav"
    p "Sara se alista para ir a la escuela, está muy animada"
    s "[name] crees que deba cambiar de imagen?"
    menu:
        "NO, estas bien asi.":

            jump estas_bien_asi

        "un cambio daria una nueva imprecion.":

            jump un_cambio_daria_una_nueva_imprecion

label estas_bien_asi:
    hide ilustracion23-4
    show ilustracion23-3
    with dissolve
    s "tienes razón"
    s "tengo que ser yo misma si quiero hacer más amigos"
    hide ilustracion23-3
    show colegioejm1
    with dissolve
    p "nos dirigimos a la escuela después del desayuno"
    p "hoy está nublado"
    p "en la clase de Manualidades el profesor pidió hacer un grupo para realizar
    una maqueta de cualquier paisaje"
    p "parece ser que todos ya tienen parejas"
    s "bueno parece ser que hoy toca hacer sola.."
    scene ilustracion19
    hide colegioejm1
    show ilustracion19-3
    with dissolve
    g "Sara... no tienes compañero?"
    s "mm.."
    g "hagamos equipo"
    hide ilustracion19-3
    show ilustracion19-4
    with dissolve
    g "si.., resulta que estaba distraída y no me dio tiempo de buscar un compañero"
    g "jejeje..."
    p "en el recreo Sara y Gabriela se quedaron en el aula hablando de cómo sería
    el paisaje para realizar la maqueta"
    hide ilustracion19-4
    show ilustracion19-2
    with dissolve
    g "bueno y donde lo realizamos?"
    s "como?"
    g "qué te parece si lo realizas en tu casa"
    s "bueno..."
    hide ilustracion19-2
    show ilustracion19-1
    with dissolve
    g "no te preocupes jeje."
    s "se lo diré a mis padres"
    p "en medio de la plática uno de los compañeros entró con sus amigos y se nos
    acercó"

    play music "sound/emotional-piano.mp3"
    scene ilustracion
    hide ilustracion19-1
    show ilustracion26-2
    with dissolve
    n "¿ Cómo puedes estar con esa niña RARA!!?"
    n "O se te pego lo rara también?"
    g "no es rara y déjanos!"
    n "claro las dejo, pero antes..."
    p "en eso el niño da una señal a sus amigos y agarran a Sara y Gabriela"
    hide ilustracion26-2
    show ilustracion32_5
    with dissolve
    p "el niño empieza a vaciar sus mochilas desparramando sus cosas por el suelo"
    p "todos lo veían pero nadie quería hacer nada"
    n "Será mejor que empieces a escoger bien a tus amistades Gabriela."
    hide ilustracion32_5
    show ilustracion36
    with dissolve
    p "cuando las soltaron, Sara corrió por todos lados recogiendo las pertenencias
    de Gabriela"
    s "losiento."
    s "en verdad lo siento"#llorando
    s "si no estuvieras conmigo esto no te estaria pasando"
    g "porque te disculpas"
    hide ilustracion36
    show ilustracion36-1
    with dissolve
    s "...?"
    g "es lo que yo decidí, no te preocupes"
    p "Gabriela recogió las cosas de Sara y se alistaron para la siguiente clase"
    #sara calmo sus lagrimas
    hide ilustracion36-1
    show ilustracion27-1
    with dissolve
    play music "sound/nocheambiente.wav"
    p "en la noche cuando llegaron los padres de Sara"
    p "Sara se dirigió a su padre para decirle que vendrá Gabriela el Sábado
    pero su padre le dijo que hablara con su madre"
    s "Mamá mañana vendra una amiga para hacer un trabajo"
    pm "Estabien hija, puedes pasarme la libreta azul de la mesa?"

    hide ilustracion27-1
    show ilustracion23-5
    with dissolve
    p "sara se fue a dormir para recibir el gran dia, no podia esperar"
    hide ilustracion23-5
    show ilustracion91-1
    with dissolve
    play music "sound/happy-sandbox.wav"
    p "EN LA TARDE"
    p "tocaron la puerta y Sara fue a recibir a gabriela"
    hide ilustracion91-1
    show ilustracion91-2
    with dissolve
    pg "hola buenas tardes"
    pg "tú debes ser Sara"
    s "..si.. buenas tardes."
    pg "tus padres están en casa?"
    s "no, salieron a trabajar."
    hide ilustracion91-2
    show ilustracion91-3
    with dissolve
    g "Papá ya déjanos.. puedes irte"
    pg "ok ok cuidate ok hija."
    g "si papá estaré bien"
    pg "esta bien, pasare por ti en la noche"
    hide ilustracion91-3
    scene ilustracion23
    show ilustracion23-6
    with dissolve
    p "el padre de Gabriela se fue y las dos comenzaron a realizar la maqueta"
    g "tus padres... solo hoy salieron?"
    s "bueno.. salen todo los días."
    g "espera!"
    g "osea que estas sola todos los días"
    s "si, pero no me molesta ya estoy acostumbrada"
    g "ya veo"
    g "eres realmente sorprendente."
    g "pero... no estas sola con [name]"
    s "Quien?"
    s "Ha! si."
    s "siempre esta a mi lado"
    hide ilustracion23-6
    show ilustracion92
    with dissolve
    p "fue un arduo trabajo realizar la maqueta pero por fin lo terminaron"
    g "PORFIN!!!..."
    g "parece que quedo bien"
    s "eso parece"
    s "voy por algunos refrigerios"
    hide ilustracion92
    show ilustracion93
    with dissolve
    p "llegando a ser las 8:00 de la noche el padre de gabriela toco la puerta"
    hide ilustracion93
    show ilustracion91-4
    with dissolve
    pg "perdón por la tardanza se me fue la hora"
    g "Aun no llegan tus padres?"
    pg "Enserio? estarás bien sola?"
    s "si, no se preocupe estaré bien."
    g "bueno cuidate Sara"
    hide ilustracion91-4
    show ilustracion91-5
    with dissolve
    p "Sara se despide de Gabriela"
    s "ahora.."
    s "estoy sola."
    s "No!.. tengo amigos a mi lado"
    #cap 5
    play music "sound/ambienteascensor.wav"
    hide ilustracion91-5
    show ilustracion27-2
    with dissolve
    p "ya es Lunes"
    p "Sara se alista y lleva la maqueta a su escuela"
    p "al llegar vemos a gabriela en su asiento y la saludamos
    se ven muy felices"
    scene ilustracion19
    hide ilustracion27-2

    show ilustracion19-10
    with dissolve
    s "aqui esta la maqueta"
    g "que bien.. ya solo queda presentarlo"
    scene ilustracion
    hide ilustracion19-10
    show ilustracion31-1
    with dissolve
    m "muy bien Alumnos, los trabajos lo presentaremos al final de la clase
    para que lo vean los otros cursos"
    hide ilustracion31-1
    show ilustracion18
    with dissolve
    p "Comenzaron con la clase hasta que toco el timbre de recreo y todos salieron
    al patio"
    s "Crees que quedo bien?"
    g "yo creo q quedo fantastico"
    s "esque..."
    g "Sara, realizamos juntas este trabajo"
    s "si tienes razon"
    hide ilustracion18
    show ilustracion10-1
    with dissolve
    play music "sound/arpeggio-mess.wav"
    p "Cuando regresamos al aula vimos el trabajo de Sara y Gabriela
    partido en dos y destrozado"
    show ilustracion94
    with dissolve
    p "alrededor solo se escuchaban burlas"
    p "Sara no podía resistir y cayó en lágrimas entre el suelo y todo
    alrededor sólo parecía ser burlas y llanto"
    p "Gabriela molesta se dirigió hacia el niño"
    hide ilustracion10-1
    hide ilustracion94
    show ilustracion95
    with dissolve
    g "Fuiste tu?"
    n "Y que si fui yo."
    n "no puedes hacer nada al respecto porque todos aquí.."
    hide ilustracion95
    show ilustracion96
    with dissolve
    p "el niño fue empujado tan fuerte que cayó entre los asientos"
    hide ilustracion96
    show ilustracion97
    with dissolve
    p "entre ellos se ve una pelea pero los estudiantes van a detener a Gabriela
    socorriendo al niño"
    p "el niño molesto viendo a Gabriela vulnerable se le acerca con furia
    pero en eso se escucha una voz frágil."
    hide ilustracion97
    show ilustracion98
    with dissolve
    play music "sound/cheesepuff.mp3"
    s "porque?"
    s "porque me odias?"
    s "PORQUE TODOS ME ODIAN TANTO?"
    p "Todos los estudiantes se quedaron en silencio y Gabriela le gritó al niño"
    hide ilustracion98
    show ilustracion99
    with dissolve
    g "SARA SIEMPRE ESTÁ SOLA!!!"
    g "Sus padres nunca están con ella"
    g "y tiene que venir aquí solo para soportar a personas como tu"
    g "A ti te hace feliz hacerle esto?!!.."
    n "yo... no lo sabía"
    n "Mis padres se separaron"
    hide ilustracion99
    show ilustracion10-1
    with dissolve
    p "todos los niños sintieron culpa por las cosas que le hicieron a Sara"
    p "Gabriela comenzó a recoger los trozos de la maqueta y en ese momento los
    demás comenzaron a ayudar a repararla"
    p "Sara solo estaba en su lugar deprimida"
    hide ilustracion10-1
    show ilustracion100
    with dissolve
    play music "sound/emotional.mp3"
    g "Sara?"
    g "terminamos la Maqueta."
    hide ilustracion100
    show ilustracion102
    with dissolve
    p "sara levantó la mirada y vio a todos los niños rodeandola"
    hide ilustracion102
    show ilustracion103
    with dissolve
    n "P...pe...PERDON!!!"
    hide ilustracion103
    show ilustracion104
    with dissolve
    ns "Lo siento Sara. perdón Sara. yo también te pido perdon"
    hide ilustracion104
    show ilustracion105
    with dissolve
    ns "LO SENTIMOS MUCHO SARA!!!!!"
    p "Sara realmente no lo podía creer."
    p "cuando vio la maqueta, noto que había muchas cosas en ella"
    p "Fue uno de los momentos más emotivos en la vida de Sara."
    hide ilustracion105
    show colegioejm
    with dissolve
    p "Después de terminar las Clases todos se fueron a sus casas."
    g "Crees que la maqueta quedó bien?"
    s "Yo creo que quedó..."
    hide colegioejm
    show ilustracion106
    with dissolve
    s "Muy bonita"
    "FINAL BUENO"

    #Final bueno de la novela
    return
label no_es_necesario:
    s "si, no veo el porque tendría que ser como gabriela"
    s "Ella tiene su forma de ser con los demás"
    s "continuaré con mi forma de ser"
jump deberias_dejarlo
label deberias_dejarlo1:
    s "todo esto es inutil"
label deberias_dejarlo:
    p "y asi surgio hasta que termino la clase"
    p "tras recoger sus cosas se topó con sus compañeros de curso"
    hide ilustracion112
    show ilustracion108
    with dissolve
    play music "sound/pianoambient.mp3"
    n "Sara... sigues sola"
    s "No estoy sola"
    s "Estoy con [name]"
    n "Sigues con ese jueguito niña rara?"
    hide ilustracion108
    show ilustracion107
    with dissolve
    p "El niño da una señal y los otros compañeros sujetaron a Sara"
    p "Mientras el otro niño buscaba todo el dinero que tenía Sara"
    p "Tomo su mochila y removió entre su cosas"
    n "tch...... , ¿Solo eso?"
    n "Bueno para algo servirá"
    s "Porfavor... devuelveme mi dinero"
    s "Lo necesito para volver a mi casa"
    p "Los niños con la sonrisa marcada en sus caras se van del aula"
    n "Dile a tu amigo que te preste
    Jajaja..."
    hide ilustracion107
    show ilustracion113
    with dissolve
    p "Sara se veía humillada después de lo ocurrido"
    s "[name]?"
    s "Por que nos tratan tan mal?"
    g "Nos?"
    hide ilustracion113
    show ilustracion114
    with dissolve
    p "Sara levantó la mirada y vio Gabriela delante de ella"
    g "Por que te tratan tan mal tus compañeros?"
    s "Es por que no pueden ver a [name]"
    g "[name]?"
    s "Si, el es mi amigo"
    g "Bueno, pues [name] no debería dejarte sola"
    s "No estoy sola."
    g "Bueno, ¿ quieres ir a tomar un helado?"
    s "Mmmm.. Lo siento me quitaron mi dinero"
    s "No tengo para volver a mi casa"
    hide ilustracion114
    show ilustracion115
    with dissolve
    g "......... Toma!"
    g "Supongo que el helado será para otro rato"
    s "Gracias!!"
    g "No te preocupes"
    g "Ya me tengo que ir, nos vemos mañana"
    hide ilustracion115
    show ilustracion116
    with dissolve
    p "Sara se fue a su casa, parece estar mejor de lo ocurrido"
    p "Realmente esos son los gestos que pueden cambiar
    el estado de ánimo de la gente"
    p "Sara se fue a dormir más tranquila"
    hide ilustracion116
    show ventanaejm
    with dissolve
    p "Ya es de dia y Sara se pone su uniforme de educación física para salir"
    s "Vamos!! [name]"
    scene ilustracion9-1
    hide ventanaejm

    show ilustracion9-3
    with dissolve
    play music "sound/fondo-cole.wav"
    p "Todos salimos al patio para empezar la clase"
    m "Bien, para el ejercicio de hoy trabajaremos con un compañero
    para que nos apoye"
    s "[name] debo hablar para el ejercicio de hoy, crees que sea.."

    menu:
        "Es una buena idea.":
            jump es_una_buena_idea1

        "No creo necesario.":
            jump no_creo_necesario


label no_creo_necesario:

    hide ilustracion9-3
    show ilustracion9-4
    with dissolve
    s "Cierto, lo que paso ayer solo fue porque me tenia lastima
    mejor trabajo con [name]"

    hide ilustracion9-4
    with dissolve
    p "Empezamos a trabajar toda la clase solos, fue algo cansador"
    hide ilustracion9-1
    show ilustracion117
    with dissolve
    p "después de la clase fuimos a comprarnos algo en la salida
    pero nos topamos otra vez con los niños"
    play music "sound/arpeggio-mess.wav"
    n "Hola.."
    p "Sara sentía otra vez aquel miedo de lo que pueda ocurrir otra vez"
    n "donde vas sara?"
    s "yo... mm... ya me iba."
    p "el niño lanzó otra vez una señal y los otros sujetaron nuevamente a sara"
    hide ilustracion117
    show ilustracion107
    with dissolve
    n "vaya!"
    n "parece que ahora tienes más"
    s "devuélvemelo por favor!"
    n "Claro! toma!.."
    p "El niño arrojó sus monedas a los aires y se va con sus amigos"
    hide ilustracion107
    show ilustracion118
    with dissolve
    s "No debo llorar"
    s "asi sera siempre"
    s "solo debo ser mas fuerte"
    s "tengo que empezar a valerme por mi misma"
    p "Parece que Sara acepto lo que le deparará el futuro
    no crei que llegaria a olvidarme de esta forma"
    p "Espero que le vaya bien en toda su vida"
    "FINAL NEUTRAL"
    #final neutral de la novela
    return
label es_una_buena_idea1:
    s "Si, tienes razón creo que es un buen momento para intentar
    llevarme bien con ella"

    hide ilustracion9-3
    with dissolve
    p "Sara está decidida  en preguntar a Gabriela para formar equipo"
    p "quizá esto sea algo bueno para ella, pero tengo el presentimiento que
    algo malo va a pasar"
    hide ilustracion9-1
    show ilustracion9-5
    with dissolve
    s "Gabriela."
    s "Yo... mm..."
    g "Si?"
    s "queria saber si quieres ser mi compañera de educacion fisica"
    p "ese momento se convirtió en un ambiente silencioso"
    g "Emm... bueno..."
    n "¡Qué haces aquí niña rara!"
    n "quieres seguir incomodando?"
    s "yo.. no."

    hide ilustracion9-5
    show ilustracion119
    with dissolve
    g "Oye..! no la molestes."
    n "Ella es la rara, no tiene porque estar con nosotros"
    n "Vamos muévete, vete con tu amigo raro."
    p "Gabriela se ve molesta por el mal trato que recibe Sara"
    p "Pero a Sara solo la puedo ver sumisa"
    s "Lo Siento por molestar"
    n "Gabriela."
    n "Si lo que quieres es tener amigos"
    n "te recomiendo que escojas bien tus amistades"
    hide ilustracion119
    show ilustracion9-6
    with dissolve
    p "No entiendo porque hay tanta indiferencia hacia sara"
    p "Ella no es una mala persona, solo quiere ser como los demás"
    play music "sound/emotional.mp3"
    g "SARA!!!.."#CORRIENDO

    p "Se oyó un grito en la multitud"
    hide ilustracion9-6
    show ilustracion120
    with dissolve
    g "aun te falta compañero?"
    p "Sara no lo podía creer pues ella ya se estaba resignando a continuar sola
    pero ese grito pudo despertarla de su pesar."
    hide ilustracion120
    show ilustracion124
    with dissolve
    p "al dia siguiente"
    p "después de lo ocurrido Sara se ve mas confiada de lo normal"
    p "Parece que ahora tendrá un amigo con quien hablar"
    s "Aun no puedo creer lo que paso ayer"
    s "yo.. nose que hacer."
    s "tengo que irme"
jump final_malo
label un_cambio_daria_una_nueva_imprecion:
    s "si, talvez cambie de corte de cabello."
    s "Ya se hace tarde tengo que irme!!"
label final_malo:
    scene fondo2
    hide ilustracion124

    show ilustracion32_1
    with dissolve
    play music "sound/ambienteascensor.wav"
    p "Sara llegando al colegio noto la mirada de los estudiantes
    algo escalofriante e intimidante"
    g "Sara que tal estas"
    g "buenos días"
    s "Buenos días"
    g "toma asiento"
    g "ya va a comenzar la clase"

    hide ilustracion32_1
    scene ilustracion
    show ilustracion31-6
    with dissolve
    m "muy bien niños... para el lunes necesito que hagan una maqueta sobre
    algún paisaje"
    m "puede ser en grupos de a dos"
    s "mm... parece que..."
    scene ilustracion19
    hide ilustracion31-6
    show ilustracion19-3
    with dissolve
    g "hacemos equipo?"
    hide ilustracion19-3
    show ilustracion19-4
    with dissolve
    s "Si!"
    p "Sara estaba algo nerviosa"
    p "no sabia que hacer o qué decir"
    g "Qué tipo de paisaje deberíamos poner"
    hide ilustracion19-4
    show ilustracion19-2
    with dissolve
    g "y también en que casa lo deberíamos realizar"
    g "Sara donde vives?"
    s "yo... vivo en Ticti Norte"
    g "más o menos por donde"
    s "casi llegando a la entrada del parque Tunari"
    g "ENSERIO!!"
    g "Podemos hacer de eso la maqueta"
    s "Bueno... yo creo que si"
    hide ilustracion19-2
    show ilustracion19-1
    with dissolve
    g "Bien! quedamos en tu casa verdad"
    s "Si! se lo diré a mis padres"
    #en casa
    hide ilustracion36-1
    show ilustracion27-1
    with dissolve
    play music "sound/nocheambiente.wav"
    s "Papá?"
    ph "ahora no hija"
    s "Mamá?"
    pm "Si?"
    s "Mañana..."
    pm "Cariño puedes pasarme la libreta azul?"

    s "Mañana vendrá una amiga a realizar una maqueta"
    pm "Si amor los amigos que quieras"
    ph "Amor se hace tarde"
    pm "Ya voy!.."
    pm "te calientas la cena, está en el microondas"
    pm "Te quiero."
    hide ilustracion27-1
    show ilustracion23-5
    with dissolve
    p "Los padres de Sara se fueron y Sara se volvió a quedar sola pero anciosa
    por lo de mañana."
    hide ilustracion23-5
    show ilustracion91-1
    with dissolve
    ####
    play music "sound/happy-sandbox.wav"
    p "EN LA TARDE"
    p "tocaron la puerta y Sara fue a recibir a gabriela"
    hide ilustracion91-1
    show ilustracion91-2
    with dissolve
    pg "hola buenas tardes"
    pg "tú debes ser Sara"
    s "..si.. buenas tardes."
    pg "tus padres están en casa?"
    s "no, salieron a trabajar."
    hide ilustracion91-2
    show ilustracion91-3
    with dissolve
    g "Papá ya déjanos.. puedes irte"
    pg "ok ok cuidate ok hija."
    g "si papá estaré bien"
    pg "esta bien, pasare por ti en la noche"
    scene ilustracion23
    hide ilustracion91-3

    show ilustracion23-6
    with dissolve
    p "el padre de Gabriela se fue y las dos comenzaron a realizar la maqueta"
    g "tus padres... solo hoy salieron?"
    s "bueno.. salen todo los días."
    g "espera!"
    g "osea que estas sola todos los días"
    s "si, pero no me molesta ya estoy acostumbrada"
    g "ya veo"
    g "eres realmente sorprendente."
    g "pero... no estas sola con [name]"
    s "Quien?"
    s "Ha! si."
    s "siempre esta a mi lado"
    hide ilustracion23-6
    show ilustracion92
    with dissolve
    p "fue un arduo trabajo realizar la maqueta pero por fin lo terminaron"
    g "PORFIN!!!..."
    g "parece que quedo bien"
    s "eso parece"
    s "voy por algunos refrigerios"
    hide ilustracion92
    show ilustracion93
    with dissolve
    p "llegando a ser las 8:00 de la noche el padre de gabriela toco la puerta"
    hide ilustracion93
    show ilustracion91-4
    with dissolve
    pg "perdón por la tardanza se me fue la hora"
    g "Aun no llegan tus padres?"
    pg "Enserio? estarás bien sola?"
    s "si, no se preocupe estaré bien."
    g "bueno cuidate Sara"
    hide ilustracion91-4
    show ilustracion91-5
    with dissolve
    p "Sara se despide de Gabriela cuando ya está en el auto"
    s "ahora.."
    s "estoy sola."
    s "No!.. tengo amigos a mi lado"
    hide ilustracion91-5
    show ilustracion125
    with dissolve
    play music "sound/major.mp3"
    p "Al día siguiente Sara se pone pensativa de como cambiar su cabello"
    p "Así que ella va á buscar á su madre pero ella se encontraba ocupada"
    s "Mamá...?"
    pm "Ahora no hija, tengo que preparar estos documentos para mañana"
    p "Sara no tenía opción que hacerlo ella sola"
    p "Aunque le tomó mucho tiempo se veía muy bonita"
    hide ilustracion125
    show ilustracion126
    with dissolve
    play music "sound/major.mp3"
    p "Cuando Sara llegó a la escuela, todos los niños vieron
    el Gran cambio de Sara e incluso Gabriela quedo sorprendida"
    s "Hola"
    g "Hola sara!, te ves diferente"
    s "Quería cambiar un poco"
    g "Te ves bien"
    p "Esto llamó mucho la atención de lo niños"
    hide ilustracion126
    show ilustracion18
    with dissolve
    p "Ya después de haber presentado los trabajos alistaron sus cosas
    para irse pero en ese momento"
    play music "sound/166748__afleetingspeck__haunting-sequence-in-g-or-ab.mp3"

    n "Que bien te ves Sara"
    p "Sara y Gabriela son inmovilizadas por los niños y en el acto
    vacían sus mochilas y del suelo levantan una tijera"
    hide ilustracion18
    show ilustracion127
    with dissolve
    n "Déjame arreglarte el cabello!"
    hide ilustracion127
    show ilustracion128
    with dissolve
    p "Agarra a Sara y le corta el cabello
    mechon por mechon."
    p "Sara no podía hacer nada estaba totalmente en shock"
    p "Todos veían como se le caia el cabello"
    n "Listo ahora te ves bien"
    hide ilustracion128
    show ilustracion129
    with dissolve
    p "Todos se rieron y Sara quedó humillada"
    p "Entre todas las risas Sara se fue lentamente y tomo su movilidad"
    p "Pero no fue a su casa, llegó a la parada y subió lo más alto
    del Parque tunari"
    p "Camino hasta que oscureció"
    hide ilustracion129
    show ilustracion130
    with dissolve
    p "Cuando se dio cuenta de la luz de la luna
    comenzó a llorar."
    hide ilustracion130
    show ilustracion132
    with dissolve
    play music "sound/sad-piano-remix.mp3"
    s "Porque, porque, porque, porque, porque, porque."
    hide ilustracion132
    show ilustracion131
    with dissolve
    s "Yo no hice nada malo"
    s "Yo no quiero esto"
    p "No llores sara yo estaré siempre a tu lado"
    hide ilustracion131
    show ilustracion133
    with dissolve
    s "[name]!!?"
    hide ilustracion133
    show ilustracion134
    with dissolve
    p "Sara me vio y corrió hacia mi."

    p "por fin estuvimos juntos"
    "FINAL MALO"

    #Final malo
    return
    # Finaliza el juego:
    return
