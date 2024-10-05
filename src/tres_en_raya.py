from src.support_tres_en_raya import *

def tres_en_raya():

    matriz_tablero = inicializar_tablero()
    jugador_actual = "X"
    juego_activo = True

    print("Tres en Raya")
    print("Selecciona el modo de juego:")
    print("1. Dos jugadores")
    print("2. Jugar contra la máquina")
    
    modo_game = input("Elige una opción (1 o 2): ")

    while juego_activo:
        mostrar_tablero(matriz_tablero)
        print(f"Turno del jugador: {jugador_actual}")

        if modo_game == '1' or (modo_game == '2' and jugador_actual == 'X'):
            # Movimiento del jugador humano
            try:
                fila = int(input("Ingresa la fila (0, 1, 2): "))
                columna = int(input("Ingresa la columna (0, 1, 2): "))
            except:
                print("valor introducido, no es correcto")
                juego_activo = False

            if juego_activo == True:
                if (fila != 0 or fila!= 1 or fila != 2) and (columna != 0 or columna!= 1 or columna != 2):
                    if realizar_movimiento(matriz_tablero, fila, columna, jugador_actual):
                        # Verificar si hay ganador o empate
                        if verificar_victoria(matriz_tablero):
                            mostrar_tablero(matriz_tablero)
                            print(f"¡Jugador {jugador_actual} ha ganado!")
                            juego_activo = False
                        elif tablero_lleno(matriz_tablero):
                            mostrar_tablero(matriz_tablero)
                            print("¡Es un empate!")
                            juego_activo = False
                        else:
                            jugador_actual = cambiar_turno(jugador_actual)

        elif modo_game == '2' and jugador_actual == 'O':
            # Movimiento de la máquina
            print("Turno de la máquina:")
            movimiento_maquina(matriz_tablero)
            # Verificar si hay ganador o empate
            if verificar_victoria(matriz_tablero):
                mostrar_tablero(matriz_tablero)
                print("¡La máquina ha ganado!")
                juego_activo = False
            elif tablero_lleno(matriz_tablero):
                mostrar_tablero(matriz_tablero)
                print("¡Es un empate!")
                juego_activo = False
            else:
                jugador_actual = cambiar_turno(jugador_actual)

        # Ofrecer la opción de reiniciar el juego
        if not juego_activo:
            jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
            if jugar_otra == 's':
                matriz_tablero, jugador_actual, juego_activo = reiniciar_juego()
                modo_game = input("Elige una opción (1 o 2): ")
            else:
                break