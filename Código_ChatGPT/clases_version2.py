
import numpy as np
import random
from variables_version2 import DIMENSIONES, SIMBOLOS

class Barco:
    def __init__(self, nombre, eslora):
        """
        Inicializa un objeto de la clase Barco con su nombre y eslora.
        
        Args:
            nombre (str): El nombre del barco.
            eslora (int): La eslora del barco.
        """
        self.nombre = nombre
        self.eslora = eslora
        self.coordenadas = []
        self.impactos = 0

    def registrar_impacto(self):
        """
        Registra un impacto en el barco, incrementando el contador de impactos.
        """
        self.impactos += 1

    def esta_hundido(self):
        """
        Verifica si el barco ha sido hundido.
        
        Un barco se considera hundido si ha recibido tantos impactos
        como su eslora. En ese caso, regresa True.
        
        Returns:
            bool: True si el barco ha sido hundido, False de lo contrario.
        """
        return self.impactos >= self.eslora

class Tablero:
    def __init__(self, id_jugador, dimensiones, barcos, es_maquina = False):
        """
        Inicializa un objeto de la clase Tablero.

        Args:
        id_jugador (str): Identificador del jugador (puede ser "Jugador" o "Máquina").
        dimensiones (tuple): Dimensiones del tablero (filas, columnas).
        barcos (dict): Diccionario de barcos con el nombre como clave y la eslora como valor.
        es_maquina (bool, opcional): Indica si el tablero pertenece a la máquina. Por defecto es False.

        Atributos:
        id_jugador (str): Identificador del jugador.
        dimensiones (tuple): Dimensiones del tablero.
        barcos (list): Lista de objetos Barco presentes en el tablero.
        tablero_visible (np.ndarray): Vista del tablero visible para el jugador.
        tablero_oculto (np.ndarray): Tablero con la disposición real de los barcos.
        es_maquina (bool): Indica si el tablero pertenece a la máquina.
        vidas (int): Número total de esloras de todos los barcos en el tablero.
        """
        self.id_jugador = id_jugador
        self.dimensiones = dimensiones
        self.barcos = [Barco(nombre, eslora) for nombre, eslora in barcos.items()]
        self.tablero_visible = np.full(dimensiones, SIMBOLOS["agua"])
        self.tablero_oculto = np.full(dimensiones, SIMBOLOS["agua"])
        self.es_maquina = es_maquina
        self.vidas = sum(barco.eslora for barco in self.barcos)

    def inicializar_tablero(self):
        """
        Inicializa el tablero colocando todos los barcos en posiciones aleatorias.

        Para cada barco en la lista de barcos, se selecciona una orientación y una
        posición inicial aleatoria en el tablero. Intenta colocar el barco en el 
        tablero hasta que encuentra una posición válida.

        La orientación puede ser horizontal ("H") o vertical ("V"). La posición 
        inicial se elige aleatoriamente dentro de los límites del tablero.
        """
        for barco in self.barcos:
            while True:
                orientacion = random.choice(["H", "V"])
                fila = random.randint(0, self.dimensiones[0] - 1)
                columna = random.randint(0, self.dimensiones[1] - 1)
                if self.colocar_barco(barco, fila, columna, orientacion):
                    break

    def colocar_barco(self, barco, fila, columna, orientacion):
        """
        Intenta colocar un barco en el tablero en la posición especificada.

        Args:
            barco (Barco): El objeto barco que se va a colocar.
            fila (int): La fila inicial para colocar el barco.
            columna (int): La columna inicial para colocar el barco.
            orientacion (str): La orientación del barco, puede ser "H" para horizontal o "V" para vertical.

        Returns:
            bool: True si el barco se colocó exitosamente, False si no fue posible colocarlo.
        """
        coordenadas = []
        for i in range(barco.eslora):
            if orientacion == "H":
                if columna + barco.eslora > self.dimensiones[1]:
                    return False
                coordenadas.append((fila, columna + i))
            elif orientacion == "V":
                if fila + barco.eslora > self.dimensiones[0]:
                    return False
                coordenadas.append((fila + i, columna))
        if any(self.tablero_oculto[x, y] == SIMBOLOS["barco"] for x, y in coordenadas):
            return False
        for x, y in coordenadas:
            self.tablero_oculto[x, y] = SIMBOLOS["barco"]
        barco.coordenadas = coordenadas
        return True

    def disparar(self, x, y):
        """
        
        """
        if self.tablero_visible[x, y] != SIMBOLOS["agua"]:
            print("Ya disparaste aquí.")
            return "repetido"
        if self.tablero_oculto[x, y] == SIMBOLOS["barco"]:
            self.tablero_visible[x, y] = SIMBOLOS["impacto_barco"]
            self.tablero_oculto[x, y] = SIMBOLOS["impacto_barco"]
            for barco in self.barcos:
                if (x, y) in barco.coordenadas:
                    barco.registrar_impacto()
                    self.vidas -= 1
                    if barco.esta_hundido():
                        return "hundido"
                    return "impacto"
        else:
            self.tablero_visible[x, y] = SIMBOLOS["impacto_agua"]
            return "agua"

    def disparar_aleatorio(self):
        """
        
        """
        while True:
            x = random.randint(0, self.dimensiones[0] - 1)
            y = random.randint(0, self.dimensiones[1] - 1)
            if self.tablero_visible[x, y] == SIMBOLOS["agua"]:
                resultado = self.disparar(x, y)
                if resultado == "agua":
                    print(f"La máquina disparó a ({x}, {y}) y falló.")
                elif resultado == "impacto":
                    print(f"La máquina disparó a ({x}, {y}) y acertó.")
                elif resultado == "hundido":
                    print(f"La máquina disparó a ({x}, {y}) y hundió un barco.")
                break

    def imprimir_tablero(self):
        """
        
        """
        for fila in self.tablero_visible:
            print(" ".join(fila))
