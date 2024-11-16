
import numpy as np
import random

class Barco:
    def __init__(self, nombre, eslora):
        self.nombre = nombre
        self.eslora = eslora
        self.coordenadas = []
        self.impactos = 0

    def colocar(self, coordenadas):
        self.coordenadas = coordenadas

    def recibir_impacto(self):
        self.impactos += 1
        return self.impactos >= self.eslora


class Tablero:
    def __init__(self, id_jugador, dificultad):
        self.id_jugador = id_jugador
        self.dificultad = dificultad
        self.tamaño = 10
        self.tablero = np.full((self.tamaño, self.tamaño), '~')
        self.tablero_oculto = np.full((self.tamaño, self.tamaño), '~')
        self.barcos = []
        self.vidas = 0

    def colocar_barcos(self):
        barcos_config = {"Barco1": 4, "Barco2": 3, "Barco3": 3, 
                         "Barco4": 2, "Barco5": 2, "Barco6": 2,
                         "Barco7": 1, "Barco8": 1, "Barco9": 1, "Barco10": 1}
        for nombre, eslora in barcos_config.items():
            barco = Barco(nombre, eslora)
            colocado = False
            while not colocado:
                x = random.randint(0, self.tamaño - 1)
                y = random.randint(0, self.tamaño - 1)
                orientacion = random.choice(["H", "V"])
                coordenadas = self.generar_coordenadas(x, y, eslora, orientacion)
                if coordenadas and self.validar_espacio(coordenadas):
                    barco.colocar(coordenadas)
                    for cx, cy in coordenadas:
                        self.tablero[cx][cy] = 'B'
                    self.barcos.append(barco)
                    self.vidas += eslora
                    colocado = True

    def generar_coordenadas(self, x, y, eslora, orientacion):
        if orientacion == "H" and y + eslora <= self.tamaño:
            return [(x, y + i) for i in range(eslora)]
        elif orientacion == "V" and x + eslora <= self.tamaño:
            return [(x + i, y) for i in range(eslora)]
        return None

    def validar_espacio(self, coordenadas):
        return all(self.tablero[x][y] == '~' for x, y in coordenadas)

    def disparar(self, x, y):
        if self.tablero[x][y] == 'B':
            self.tablero[x][y] = 'X'
            self.tablero_oculto[x][y] = 'X'
            for barco in self.barcos:
                if (x, y) in barco.coordenadas:
                    hundido = barco.recibir_impacto()
                    if hundido:
                        print(f"¡Barco {barco.nombre} hundido!")
                        self.vidas -= barco.eslora
                    return True
        elif self.tablero[x][y] == '~':
            self.tablero[x][y] = 'O'
            self.tablero_oculto[x][y] = 'O'
        else:
            raise ValueError("Ya disparaste aquí.")
        return False

    def disparo_maquina(self):
        x, y = random.randint(0, self.tamaño - 1), random.randint(0, self.tamaño - 1)
        while self.tablero_oculto[x][y] != '~':
            x, y = random.randint(0, self.tamaño - 1), random.randint(0, self.tamaño - 1)
        return self.disparar(x, y)

    def imprimir_tablero(self):
        print("\n".join(" ".join(row) for row in self.tablero_oculto))
