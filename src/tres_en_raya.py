from src.support_tres_en_raya import Tres_en_raya_Support as tres

class Tres_En_Raya:

    def tres_en_raya(self):

        def __init__(self, salida):
            self.salida = salida

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
                # Movimiento del jugador humano
                try:
                    fila = int(input("Ingresa la fila (0, 1, 2): "))
                    columna = int(input("Ingresa la columna (0, 1, 2): "))
                except:
                    print("valor introducido, no es correcto")
                    control_juego = False

                if control_juego == True:
                    if (fila == 0 or fila == 1 or fila == 2) and (columna == 0 or columna!= 1 or columna != 2):
                        if tres.realizar_movimiento(tres, matriz_tablero, fila, columna, jugador_actual):
                            # Verificar si hay ganador o empate
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
                # Movimiento de la máquina
                print("Turno de la máquina:")
                tres.movimiento_maquina(tres,matriz_tablero)
                # Verificar si hay ganador o empate
                if tres.check_ganador(tres,matriz_tablero):
                    tres.mostrar_tablero(tres,matriz_tablero)
                    print("¡La máquina ha ganado!")
                    control_juego = False
                elif tres.tablero_lleno(tres,matriz_tablero):
                    tres.mostrar_tablero(tres,matriz_tablero)
                    print("¡Es un empate!")
                    control_juego = False
                else:
                    jugador_actual = tres.cambiar_turno(tres,jugador_actual)
            
            # Ofrecer la opción de reiniciar el juego
            if not control_juego:
                jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
                if jugar_otra == 's':
                    matriz_tablero, jugador_actual, control_juego = tres.reiniciar_juego(tres)
                    modo_game = input("Elige una opción (1 o 2): ")
                else:
                    break