# README - RETO HUNDIR LA FLOTA

## Introducción

Este repositorio contiene la implementación de un juego de **Hundir la flota** en Python, donde dos jugadores se enfrentan: un jugador humano y la máquina. El objetivo del juego es disparar a las posiciones del tablero enemigo para hundir sus barcos antes de que el adversario hunda los tuyos.

## Licencia

Este proyecto está disponible bajo la Licencia **MIT**. Para más detalles, consulta el archivo LICENSE.

## Requisitos

Para ejecutar este proyecto necesitarás tener instalado Python 3.x y la librería **numpy**. Si aún no tienes numpy instalada, puedes hacerlo ejecutando el siguiente comando:

```bash
pip install numpy
```

## Descripción del Juego

El juego **Hundir la Flota** consiste en lo siguiente:

- El tablero es de tamaño **10x10**.
- Cada jugador tiene los siguientes barcos:
  - 4 barcos de **1 posición**
  - 3 barcos de **2 posiciones**
  - 2 barcos de **3 posiciones**
  - 1 barco de **4 posiciones**
- Los barcos se colocan **aleatoriamente** en el tablero, aunque se puede usar una posición fija para facilitar el desarrollo.
- El jugador humano comienza disparando a una coordenada del tablero de la máquina.
  - Si el disparo **acierta**, el jugador vuelve a disparar.
  - Si el disparo **falla**, es el turno de la máquina.
- La máquina dispara a una coordenada aleatoria del tablero del jugador.
- El juego termina cuando un jugador se queda sin barcos. El otro jugador será declarado ganador.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- **main.py**: Archivo principal que ejecuta el juego.
- **clases.py**: Contiene las clases necesarias, como `Tablero`.
- **funciones.py**: Incluye funciones auxiliares, como las que gestionan los disparos.
- **variables.py**: Contiene constantes como las dimensiones del tablero y la configuración de los barcos.

## Descripción de las Clases y Funciones

### Tablero

La clase `Tablero` representa el tablero de un jugador y contiene los siguientes métodos:

- **Inicialización**: Configura el tablero con los barcos y los disparos.
- **Disparo**: Comprueba si un disparo impacta o falla y actualiza el tablero en consecuencia.
- **Visualización**: Muestra el estado actual del tablero con los impactos y los disparos fallidos.

### Métodos de Disparo

El método `disparar` se encarga de:

- Verificar si el disparo impacta en un barco o no.
- Actualizar el estado del tablero.

### main.py

Controla el flujo del juego, incluyendo:

- Mostrar las instrucciones.
- Gestionar las coordenadas de disparo del jugador.
- Alternar los turnos entre el jugador y la máquina.

### variables.py

Declara constantes clave, como:

- El tamaño del tablero.
- La configuración inicial de los barcos.

## Requisitos de Desarrollo

- **Estructura del Proyecto**: Debe incluir los siguientes archivos Python:
  - `main.py`
  - `clases.py`
  - `funciones.py`
  - `variables.py`
- **Uso de Numpy**: Los tableros se representan con matrices de `numpy` para facilitar la manipulación de datos y las operaciones relacionadas con los disparos y los barcos.

## Instrucciones para Jugar

### Inicio del Juego

El jugador humano comienza eligiendo una coordenada para disparar en el tablero de la máquina. Los turnos se alternan entre el jugador y la máquina.

### Disparo

El jugador y la máquina disparan alternadamente. Los impactos y los disparos fallidos se reflejan en sus respectivos tableros.

### Fin del Juego

El juego concluye cuando uno de los jugadores se queda sin barcos. El ganador será el jugador que conserve al menos un barco en su tablero.

## Cómo Ejecutar el Juego

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/annahico/Team-Challenge---Team-Voyager
   ```

2. Navega a la carpeta del proyecto:

   ```bash
   cd team_voyager
   ```

3. Ejecuta el archivo principal:

   ```bash
   python main.py
   ```

¡Disfruta jugando a Hundir la Flota!
