
def mostrar_instrucciones():
    print("¡Bienvenido a Batalla Naval!")
    print("Instrucciones:")
    print("- Introduce coordenadas como 'x,y' para disparar.")
    print("- Hundir todos los barcos enemigos para ganar.")
    print("- Buena suerte.\n")

def seleccionar_dificultad():
    dificultad = input("Selecciona dificultad (fácil, intermedio, difícil): ").lower()
    while dificultad not in ["fácil", "intermedio", "difícil"]:
        print("Dificultad no válida. Intenta de nuevo.")
        dificultad = input("Selecciona dificultad (fácil, intermedio, difícil): ").lower()
    return dificultad

def validar_entrada(entrada):
    try:
        x, y = map(int, entrada.split(","))
        if 0 <= x < 10 and 0 <= y < 10:
            return x, y
        else:
            print("Coordenadas fuera del rango. Intenta nuevamente.")
            return None
    except ValueError:
        print("Formato inválido. Usa 'x,y' (por ejemplo: 3,5).")
        return None

def mostrar_estado(tablero_jugador, tablero_maquina):
    print("\nTu tablero:")
    tablero_jugador.imprimir_tablero()
    print("\nTablero enemigo:")
    tablero_maquina.imprimir_tablero()

def turno_jugador(tablero_enemigo):
    coordenada = None
    while not coordenada:
        coordenada = validar_entrada(input("Introduce coordenadas para disparar (x,y): "))
    x, y = coordenada
    try:
        impacto = tablero_enemigo.disparar(x, y)
        if impacto:
            print("¡Impacto!")
            return True
        else:
            print("¡Agua!")
    except ValueError as e:
        print(e)
    return False

def verificar_ganador(tablero_jugador, tablero_maquina):
    if tablero_maquina.vidas == 0:
        print("¡Has ganado!")
        return True
    elif tablero_jugador.vidas == 0:
        print("¡La máquina ha ganado!")
        return True
    return False
