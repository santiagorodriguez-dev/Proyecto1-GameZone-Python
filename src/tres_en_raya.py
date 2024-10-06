from src.tres_en_raya_util import TresEnRayaUtil as tres

"""
    Clase que implementa el juego de Tres en Raya.

    Métodos:
        tres_en_raya() -> None:
            Inicia el juego de Tres en Raya, permitiendo seleccionar el modo de juego.
            No recibe parámetros de entrada.
            No retorna ningún valor.
            - Utiliza la clase TresEnRayaUtil para manejar la lógica del juego.
            - Permite jugar en modo de dos jugadores o contra la máquina.
"""

class TresEnRaya:

    def tres_en_raya(self):

        def __init__(self, salida):
            self.salida = salida

        try:
            matriz_tablero = tres.inicializar_tablero(tres)
            jugador_actual = "X"
            
            print("Tres en Raya")
            print("Selecciona el modo de juego:")
            print("1. Dos jugadores")
            print("2. Jugar contra la máquina")
            
            modo_game = input("Elige una opción (1 o 2): ")
            
            if modo_game != '1' and modo_game != '2':
                control_juego = False
                print("----------------")
                print("Opcion no valida")
                print("----------------")
                self.tres_en_raya()
            else:
                control_juego = True

            while control_juego:
                tres.mostrar_tablero(tres,matriz_tablero)
                print(f"Turno del jugador: {jugador_actual}")

                if modo_game == '1' or (modo_game == '2' and jugador_actual == 'X'):
                    
                    try:
                        fila = int(input("Ingresa la fila (0, 1, 2): "))
                        columna = int(input("Ingresa la columna (0, 1, 2): "))
                    except:
                        print("valor introducido, no es correcto")
                        control_juego = False

                    if control_juego == True:
                        if (fila == 0 or fila == 1 or fila == 2) and (columna == 0 or columna == 1 or columna == 2):
                            if tres.realizar_movimiento(tres, matriz_tablero, fila, columna, jugador_actual):
                                
                                if tres.check_ganador(tres,matriz_tablero):
                                    tres.mostrar_tablero(tres,matriz_tablero)
                                    print(f"¡Jugador {jugador_actual} ha ganado!")
                                    control_juego = False
                                elif tres.tablero_lleno(tres,matriz_tablero):
                                    tres.mostrar_tablero(tres,matriz_tablero)
                                    print("¡Es un empate!")
                                    control_juego = False
                                else:
                                    jugador_actual = tres.cambiar_turno(tres,jugador_actual)
                        else:
                            print("-------------------")
                            print("Posicion Incorrecta")
                            print("-------------------")
                
                elif modo_game == '2' and jugador_actual == 'O':
                    
                    print("Turno de la máquina:")
                    tres.movimiento_maquina(tres,matriz_tablero)
                    
                    if tres.check_ganador(tres,matriz_tablero):
                        tres.mostrar_tablero(tres,matriz_tablero)
                        print("¡skynet te ha ganado!")
                        control_juego = False
                    elif tres.tablero_lleno(tres,matriz_tablero):
                        tres.mostrar_tablero(tres,matriz_tablero)
                        print("¡Es un empate, que cosas!")
                        control_juego = False
                    else:
                        jugador_actual = tres.cambiar_turno(tres,jugador_actual)
                
                
                if not control_juego:
                    jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
                    if jugar_otra == 's':
                        matriz_tablero, jugador_actual, control_juego = tres.reiniciar_juego(tres)
                        modo_game = input("Elige una opción (1 o 2): ")
                    else:
                        break
        except:
            print("\n-----------------------------------------------------")
            print("Error el main principal del juego, salimos al menu")
            print("-----------------------------------------------------")