import random

from variables import SIMBOLOS


def mostrar_instrucciones():
    """
    Imprime las instrucciones del juego, incluyendo las reglas y la explicación de los símbolos.
    """
    print("\\n¡Bienvenido a Batalla Naval!")
    print("El objetivo es hundir todos los barcos del enemigo antes que hunda los tuyos.")
    print("Reglas del juego:")
    print("1. Hay un tablero de 10x10 posiciones.")
    print("2. Cada jugador tiene un conjunto de barcos colocados aleatoriamente.")
    print("3. En tu turno, ingresa las coordenadas donde quieres disparar (formato: X,Y).")
    print("4. Si aciertas en un barco enemigo, vuelves a disparar.")
    print("5. Si fallas, le toca a la máquina.")
    print("6. El juego termina cuando un jugador pierde todos sus barcos.")
    print("\\nSímbolos del tablero:")
    print(f"{SIMBOLOS['agua']} - Agua no disparada.")
    print(f"{SIMBOLOS['impacto_agua']} - Agua impactada.")
    print(
        f"{SIMBOLOS['barco']} - Barco no impactado (solo visible en tu tablero).")
    print(f"{SIMBOLOS['impacto_barco']} - Barco impactado.")
    print("\\n¡Que comience la batalla! ¡Buena suerte!")


def seleccionar_dificultad():
    """
    Permite al usuario seleccionar la dificultad del juego.
    Returns:
        int: Un número entre 1 y 3 que representa la dificultad seleccionada.
    """
    # Seleccionar la dificultad del juego
    print("Selecciona la dificultad del juego:")
    print("1. Fácil")
    print("2. Intermedio")
    print("3. Difícil")

    # Ingresar el número de la dificultad deseada
    while True:
        try:
            # Intentar convertir la entrada del usuario en un número
            nivel = int(
                input("Ingresa el número de la dificultad deseada (1-3): "))
            # Verificar si el número ingresado es válido
            if nivel in [1, 2, 3]:
                # Si es válido, regresar el número
                return nivel
            else:
                # De lo contrario, mostrar un mensaje de error
                print("Por favor, selecciona un número entre 1 y 3.")
        except ValueError:
            # Mostrar un mensaje de error si la entrada no es un número
            print("Entrada inválida. Debes ingresar un número.")


def validar_entrada(entrada):
    """
    Valida si la entrada del usuario es correcta y está dentro del rango del tablero.
    """
    try:
        x, y = map(int, entrada.split(","))
        if 0 <= x < 10 and 0 <= y < 10:
            return x, y
        else:
            print("Coordenadas fuera de rango. Deben estar entre 0 y 9.")
            return None
    except ValueError:
        print("Entrada inválida. Usa el formato X,Y (e.g., 2,3).")
        return None


def mostrar_estado(tablero_jugador, tablero_maquina):
    """
    Muestra el estado de los tableros al jugador.
    """
    print("Tu tablero:")
    tablero_jugador.imprimir_tablero()
    print("Tablero enemigo (impactos realizados):")
    tablero_maquina.imprimir_tablero()


def turno_jugador(tablero_enemigo):
    """
    Maneja el turno del jugador, solicitando coordenadas y actualizando el tablero enemigo.
    """
    while True:
        entrada = input("Ingresa las coordenadas para disparar (X,Y): ")
        coordenadas = validar_entrada(entrada)

        if coordenadas:
            x, y = coordenadas
            resultado = tablero_enemigo.disparar(x, y)
            if resultado == "agua":
                print("¡Fallaste! Le toca a la máquina.")
                break
            elif resultado == "impacto":
                print("¡Impacto! Puedes disparar de nuevo.")
            elif resultado == "hundido":
                print("¡Hundiste un barco! Puedes disparar de nuevo.")


def verificar_ganador(tablero_jugador, tablero_maquina):
    """
    Verifica si hay un ganador en el juego.
    """
    if tablero_jugador.vidas == 0:
        print("¡La máquina ha ganado! Todos tus barcos han sido hundidos.")
        return True
    elif tablero_maquina.vidas == 0:
        print("¡Felicidades! Has ganado. Todos los barcos enemigos han sido hundidos.")
        return True
    return False
