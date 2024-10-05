import random

def inicializar_tablero():
    # Crearamos el tablero
    return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
def mostrar_tablero(tablero):
    # Mostrar el tablero
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def realizar_movimiento(tablero, fila, columna, jugador):
    # movemos si es posible
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
        return True
    else:
        print("La posicion esta ocupada")
        return False

def cambiar_turno(jugador):
    # Cambiar el turno del jugador
    if jugador == "X":
        return "O"
    else:
        return "X"

def verificar_victoria(tablero):
    
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

def tablero_lleno(tablero):
    # Verificar si queda algun espacio disponible
    for fila in tablero:
        if " " in fila:
            return False
    # si llega hasta aqui es que ya esta lleno    
    return True

def movimiento_maquina(tablero):
    # Movimiento aleatorio de la máquina
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        # si no esta ocupado lo ponemos en la posicion
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            break

def reiniciar_juego():
    # Reiniciar el juego
    return inicializar_tablero(), "X", True