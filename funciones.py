import random

from variables import BOARD_SIZE, EMPTY, HIT, MISS


def print_board(board):
    # Esta función recorre el array del tablero e imprime cada fila como una cadena de caracteres.
    for row in board:
        print(" ".join(row))
    print()


def get_coordinates():
    # Esta función pide al usuario que introduzca los valores de fila y columna en un formato válido.
    # Se asegura de que las coordenadas estén dentro del rango del tablero y maneja errores de entrada.
    while True:
        try:
            user_input = input("Introduce coordenadas (fila, columna): ")
            if user_input.lower() == "salir":
                print("Saliendo del juego...")
                exit(0)  # Termina el programa si el usuario decide salir.
            x, y = map(int, user_input.split(","))
            if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                return x, y  # Devuelve las coordenadas válidas.
            else:
                print(
                    f"Coordenadas fuera del rango (0-{BOARD_SIZE-1}). Intenta de nuevo.")
        except ValueError:
            print(
                "Entrada inválida. Usa el formato: fila,columna o escribe 'salir' para abandonar.")


def player_turn(opponent_board):
    # Muestra el tablero de impactos del oponente y solicita al jugador que dispare.
    # Procesa el disparo y devuelve True si es un impacto, False si falla.
    print("Tu turno. Tablero del oponente:")
    print_board(opponent_board.hits_board)
    x, y = get_coordinates()
    # Verifica si el disparo del jugador impacta un barco.
    if opponent_board.shoot(x, y):
        print("¡Impacto!")
        return True  # Indica que el jugador tiene otro turno.
    else:
        print("Agua...")
        return False  # Finaliza el turno del jugador.


def computer_turn(player_board):
    # Genera coordenadas aleatorias para el disparo de la máquina en el tablero del jugador.
    # Procesa el disparo y devuelve True si es un impacto, False si falla.
    x, y = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
    print(f"La máquina dispara a ({x}, {y})...")
    # Verifica si el disparo de la máquina impacta un barco.
    if player_board.shoot(x, y):
        print("¡La máquina impactó!")
        return True  # Indica que la máquina tiene otro turno.
    else:
        print("La máquina falló.")
        return False  # Finaliza el turno de la máquina.
