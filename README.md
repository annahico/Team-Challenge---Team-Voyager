RETO HUNDIR LA FLOTA

## Introducción

En esta entrega vais a crear vuestra propia versión del juego de **Hundir la flota** en Python. Para el desarrollo del programa necesitarás conocimientos de la librería `numpy`, módulos, bucles, funciones, clases y colecciones de Python. **La entrega deberá constar de varios scripts de Python (archivos .py), en clase se os darán los detalles**.

## ¿Cómo funciona el juego?

Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:

1. Hay dos jugadores: tú y la máquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**

   - 4 barcos de 1 posición de eslora
   - 3 barcos de 2 posiciones de eslora
   - 2 barcos de 3 posiciones de eslora
   - 1 barco de 4 posiciones de eslora

4. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.

En [esta página](http://es.battleship-game.org/) podrás probarlo online.

## Desarrollo

Tendrás que desarrollar lo siguiente:

1. Necesitarás un conjunto de **constantes**, donde tengas inventariados los barcos del juego, dimensiones y demás variables que no vayan a cambiar que tendréis definidas en archivo de **variables.py**

2. Tendrás que construir **una clase Tablero**. Para facilitar el desarrollo, la mejor opción es desarrollar una clase tablero donde implementes las siguientes funcionalidades:

   - Cuando se inicialice deberás asignar
     - Un id de jugador, para saber de quién es el tablero.
     - Unas dimensiones de tablero, que en el fondo serán tus constantes 10 x 10.
     - Unos barcos. Los que hayas definido como constantes. Aqui simplemente puedes pasar, por ejemplo, un diccionario donde especifiques el nombre de tus barcos, y la eslora de cada uno. Luego ya los colocarás en el tablero.
     - **Un tablero sin barcos, que será un array de `numpy`** donde posicionarás los barcos. Este tablero está vacío, por lo que lo puedes rellenar de 0s, 1s, o el caracter que consideres.
     - Adicionalmente la clase tablero necesitará otro array de `numpy`, ¿por qué? porque el tablero de la maquina tendrá internamente un array con sus barcos (lo que no vemos) y hará falta otro array (que sí veremos nosotros) con los disparos efectuados, para saber dónde tenemos que disparar.
   - **Inicializar el tablero**, es decir, colocar los barcos. Puedes pasar por alto el hecho de que tengan que tener espacios entre ellos pero si los colocas aleatoriamente, mucho cuidado aquí de poner los barcos dentro del tablero, y de no colocar unos barcos encima de otros :)
   - Necesitarás un método de **disparo coordenada**. Cuando hay un disparo de un jugador en ese tablero, tendrás que comprobar si ahí había un barco, o simplemente agua. Acuérdate de marcar en el tablero, tanto si hay un impacto, como si dio agua.
   - NO te ciñas a los métodos que te acabo de mencionar, crea todos los que necesites, introduce en el constructor lo que quieras y desarrolla las funciones que consideres oportunas para facilitarte el desarrollo.

3. Una vez ya tienes modelizado tu tablero, hay que montar el programa que se ejecutara desde un **main.py**:
   - El programa no es más que el **típico `while true: `, con una serie de inputs del usuario**. Se está ejecutando constantemente y le pide al usuario coordenadas para comprobar si impacta.
   - Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
   - A continuación **inicializa los tableros de ambos jugadores** con los barcos. Estas dos primeras acciones solo se ejecutan una vez!! Que es el comienzo del juego.
   - Después de eso ya comienza el juego. Básicamente **se irá ejecutando iterativamente en el `while`, y le irá preguntando coordenadas al usuario.**
   - Recoges coordenadas, compruebas en el tablero de la máquina si habia barco.
     - Hay barco: marca en el tablero de la maquina el impacto y le vuelve a tocar al usuario
     - No hay barco: le toca a la maquina. O lo que es lo mismo, escoge una coordenada aleatoria, y comprueba en el tablero del usuario si habia barco.
   - **Así hasta que uno de los dos jugadores se quede sin barcos, y termina el juego.**
   - Cuando empiece tu turno deberías imprimir por pantalla tu tablero, para ver cuántos impactos te ha hecho la máquina, así como el tablero con los impactos que has hecho tu en el adversario, de manera que te sirva de ayuda para el siguiente disparo.
   - Todas aquellas funciones que puedas construir para la ejecución de este programa deberán estar definidas en un script que se llame **funciones.py**.

Hay infinidad de maneras para resolver este ejercicio, sentíos libres de implementarlo de la forma que te resulte más cómoda.

## Recomendaciones

1. **No es necesario tener una clase barco, aunque es recomendable** con los barcos de cada jugador, cuáles están tocados y demás. Simplemente con llevar un inventario de las coordenadas con barco es suficiente. Por ejemplo, si el tablero tuviese 2 barcos de 4 posiciones de eslora, es como si tuvieses 8 vidas. Cuando se te acaban las vidas, pierdes.
2. Para implementar el bucle `while`, puedes usar **sentencias `continue`, `break`**.
3. Se recomienda tener el código separado en **varios scripts**. Por ejemplo:
   - main.py: donde corre todo el programa
   - clases.py: aquí irán las clases
   - funciones.py: aquí irán las funciones
   - variables.py: donde están declaradas las constantes
   - A gusto del desarrollador...
4. Cuando se imprime el tablero por pantalla, básicamente será un `print()` del array de `numpy`. Escoge con sentido qué quieres que se imprima por pantalla, de manera que se vea bien dónde hay barco, donde ha habido impacto, agua... Tendrás los siguients casos:
   - Agua donde no se ha impactado
   - Agua donde se ha impactado
   - Barco donde no se ha impactado
   - Barco donde se ha impactado
5. Utiliza el `debugging` del IDE de Visual Studio Code si ves que tu programa no se comporta como debería y no sabes muy bien por qué.
6. Se recomienda en la clase tablero manejar dos arrays de 10x10. Uno con las coordenadas de los barcos y los impactos, que será tu tablero, lo que veas tu cuando imprimes tu tablero por pantalla. Y otro tablero SIN los barcos, únicamente con los impactos, para ver qué impactos has hecho en el tablero de la maquina.
7. Si vas a posicionar los barcos de manera aleatoria, tendrás que escoger unas coordenadas aleatoriamente, y una orientación N/S/E/O, de manera que si tu barco tiene 3 de eslora y la orientación es N, se posicionará hacia arriba, desde la posición inicial elegida aleatoriamente.
8. Si no tienes un nivel alto de Python, prueba primero a crear el array de numpy vacío y a colocar los barcos en unas posiciones concretas que nunca cambien, porque si lo haces aleatoriamente te será más complicado. No es justo como funciona el juego, pero mejor avanzar a quedarnos atascados al principio.

## Presentación

Cada grupo realizará una presentación en la clase de Team Challenge del **sprint 5**, donde se contarán con **20 minutos máximo**, importante ceñirse al tiempo. Se tendrá que enseñar:

1. El repositorio de github y las partes más relevantes del desarrollo de código
2. Una demo donde se muestren el funcionamiento del juego

Para esta presentación podéis apoyaros en cualquier recurso que necesites.

## Bonus track

Estos apartados NO son obligatorios.

1. Por supuesto, puedes manejar excepciones en el código todo lo que quieras, cubriendo todos los casos (por ejemplo que el usuario introduzca coordenadas fuera del tablero). Lo importante del ejercicio es que implementes el juego y que funcione. Si además de eso, consigues que tu software esté a prueba de balas, pues perfecto :)
2. No está de más que cuando sea tu turno, haya otras opciones además que la de meter coordenadas, como por ejemplo, salir del juego, que se imprima por pantalla tu tablero o el de la maquina con los impactos que has hecho.
3. Puedes introducir un nivel de dificultad que escoja el usuario al principio. Por ejemplo, el nivel de dificultad puede consistir en que cuando dispare la maquina, que lo hace de manera aleatoria, en realidad lo haga 2 o 3 veces, también aleatoriamente, y que compruebe si en alguno de esos 2 o 3 disparos, ha impactado. De esta forma, en un único disparo, la maquina tiene más posibilidades de impactarte.

**Por supuesto, pudes preguntar cualquier duda a los profesores si tienes cualquier problema con el desarrollo o no entiendes algo del enunciado :)**
