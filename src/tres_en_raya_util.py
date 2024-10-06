import random

"""
    Clase que proporciona utilidades para el juego de Tres en Raya.

    Métodos:
        inicializar_tablero() -> list:
            Inicializa y devuelve un tablero vacío de Tres en Raya.

        mostrar_tablero(tablero: list) -> None:
            Muestra el tablero en la consola.
            Parámetros:
                tablero (list): Tablero del juego, representado como una lista de listas.

        realizar_movimiento(tablero: list, fila: int, columna: int, jugador: str) -> bool:
            Realiza un movimiento en el tablero para el jugador especificado.
            Parámetros:
                tablero (list): Tablero del juego.
                fila (int): Índice de la fila donde se quiere realizar el movimiento.
                columna (int): Índice de la columna donde se quiere realizar el movimiento.
                jugador (str): Símbolo del jugador actual ("X" o "O").
            Retorna:
                bool: True si el movimiento fue exitoso, False si la posición estaba ocupada.

        cambiar_turno(jugador: str) -> str:
            Cambia el turno del jugador.
            Parámetros:
                jugador (str): Símbolo del jugador actual ("X" o "O").
            Retorna:
                str: Símbolo del siguiente jugador.

        check_ganador(tablero: list) -> bool:
            Verifica si hay un ganador en el tablero.
            Parámetros:
                tablero (list): Tablero del juego.
            Retorna:
                bool: True si hay un ganador, False en caso contrario.

        tablero_lleno(tablero: list) -> bool:
            Verifica si el tablero está lleno.
            Parámetros:
                tablero (list): Tablero del juego.
            Retorna:
                bool: True si el tablero está lleno, False si hay espacios disponibles.

        movimiento_maquina(tablero: list) -> None:
            Realiza un movimiento aleatorio para la máquina en el tablero.
            Parámetros:
                tablero (list): Tablero del juego.

        reiniciar_juego() -> tuple:
            Reinicia el juego y devuelve un nuevo tablero, el jugador inicial y un estado de juego.
            Retorna:
                tuple: Un nuevo tablero, el jugador inicial ("X"), y un estado booleano (True).
"""

class TresEnRayaUtil:

    def inicializar_tablero(self):
        return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
    def mostrar_tablero(self,tablero):
        for fila in tablero:
            print("|".join(fila))
            print("-" * 5)

    def realizar_movimiento(self,tablero, fila, columna, jugador):
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            return True
        else:
            print("La posicion esta ocupada")
            return False

    def cambiar_turno(self,jugador):
        if jugador == "X":
            return "O"
        else:
            return "X"

    def check_ganador(self,tablero):
        
        for i in range(3):
            # Verificar filas
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return True
            # Verificar columnas
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return True
        
        # verificamos diagonal 1
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return True
        # verificamos diagonal 2
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return True
        return False

    def tablero_lleno(self,tablero):
        for fila in tablero:
            if " " in fila:
                return False
        
        return True

    def movimiento_maquina(self,tablero):
        while True:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            
            if tablero[fila][columna] == " ":
                tablero[fila][columna] = "O"
                break

    def reiniciar_juego(self):
        return self.inicializar_tablero(self), "X", True