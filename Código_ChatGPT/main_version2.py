
from clases_version2 import Tablero
from funciones_version2 import (
    mostrar_instrucciones,
    seleccionar_dificultad,
    mostrar_estado,
    turno_jugador,
    verificar_ganador,
)
from variables_version2 import DIMENSIONES, BARCOS

def main():
    
    """
    Función principal del juego.
    
    Primero, muestra las instrucciones del juego y selecciona la dificultad.
    Luego, crea los tableros del jugador y la máquina y los inicializa.
    Después, inicia un bucle principal donde el jugador y la máquina se turnan
    para disparar. El juego termina cuando alguno de los dos ha ganado.
    """
    mostrar_instrucciones()
    dificultad = seleccionar_dificultad()
    tablero_jugador = Tablero(id_jugador="Jugador", dimensiones=DIMENSIONES, barcos=BARCOS)
    tablero_maquina = Tablero(id_jugador="Máquina", dimensiones=DIMENSIONES, barcos=BARCOS, es_maquina=True)
    tablero_jugador.inicializar_tablero()
    tablero_maquina.inicializar_tablero()
    juego_activo = True

    while juego_activo:
        mostrar_estado(tablero_jugador, tablero_maquina)
        print("\\nEs tu turno:")
        turno_jugador(tablero_maquina)
        if verificar_ganador(tablero_jugador, tablero_maquina):
            juego_activo = False
            break
        print("\\nTurno de la máquina:")
        tablero_jugador.disparar_aleatorio()
        if verificar_ganador(tablero_jugador, tablero_maquina):
            juego_activo = False
            break

if __name__ == "__main__":
    main()