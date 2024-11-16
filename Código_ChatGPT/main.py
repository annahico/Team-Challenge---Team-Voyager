
from clases import Tablero
from funciones import (validar_entrada, mostrar_instrucciones, 
                       seleccionar_dificultad, mostrar_estado, 
                       turno_jugador, verificar_ganador)

def main():
    mostrar_instrucciones()
    dificultad = seleccionar_dificultad()

    # Inicializar tableros
    tablero_jugador = Tablero(id_jugador="Jugador", dificultad=dificultad)
    tablero_maquina = Tablero(id_jugador="Máquina", dificultad=dificultad)

    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    while True:
        mostrar_estado(tablero_jugador, tablero_maquina)
        
        # Turno del jugador
        while turno_jugador(tablero_maquina):
            if verificar_ganador(tablero_jugador, tablero_maquina):
                return
        
        # Turno de la máquina
        print("Turno de la máquina...")
        tablero_jugador.disparo_maquina()
        if verificar_ganador(tablero_jugador, tablero_maquina):
            return

if __name__ == "__main__":
    main()
