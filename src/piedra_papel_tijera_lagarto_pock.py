from src.piedra_papel_tijera_lagarto_pock_util import PiedraPapelTijeraLagartoSpockUtil

class PiedraPapelTijeraLagartoSpock:
    """
    Clase para gestionar el juego de Piedra, Papel, Tijera, Lagarto, Spock.

    Métodos:
        jugar(): Ejecuta una partida completa del juego entre el jugador y la máquina.
        menu(): Muestra el menú principal con opciones para jugar o salir del juego.
    """

    def jugar(self):
        """
        Inicia y controla una partida de Piedra, Papel, Tijera, Lagarto, Spock.
        
        Variables:
            victorias_jugador (int): Contador de las victorias del jugador.
            victorias_maquina (int): Contador de las victorias de la máquina.
            rondas_a_ganar (int): Número de rondas que un jugador debe ganar para vencer.
            opciones (list): Lista de las opciones disponibles en el juego.
        
        Flujo:
            - El jugador elige una opción.
            - La máquina elige una opción aleatoriamente.
            - Se determina el ganador de cada ronda hasta que alguien gane el juego.
        """
        juego = PiedraPapelTijeraLagartoSpockUtil()
        victorias_jugador = 0
        victorias_maquina = 0
        rondas_a_ganar = 3

        opciones = juego.opciones

        print("¡Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock!")
        print(f"El primer jugador que gane {rondas_a_ganar} rondas, será el ganador.\n")

        
        while rondas_a_ganar > victorias_jugador and rondas_a_ganar > victorias_maquina:
            print("Opciones:")

            for i in range(5):
                print(f"{i + 1}. {opciones[i].capitalize()}")

            try:
                seleccion_jugador = int(input("Elige una opción (1-5): ")) - 1
            except ValueError:
                print("Opción no válida, intenta de nuevo.")
                continue

            if seleccion_jugador < 0 or seleccion_jugador >= len(opciones):
                print("Opción no válida, intenta de nuevo.")
                continue

            jugador_humano = opciones[seleccion_jugador]
            maquina = juego.eleccion_maquina()

            print(f"\nHas elegido: {jugador_humano.capitalize()}")
            print(f"La máquina eligió: {maquina.capitalize()}")

            ganador = juego.determinar_ganador(jugador_humano, maquina)

            if ganador == "Jugador":
                victorias_jugador += 1
                print("\n¡Ganaste esta ronda!")
            elif ganador == "Maquina":
                victorias_maquina += 1
                print("\nLa máquina ganó esta ronda.")
            else:
                print("\nEsta ronda fue un empate.")

            print(f"Marcador -> Jugador: {victorias_jugador} | Máquina: {victorias_maquina}\n")

        if victorias_jugador == rondas_a_ganar:
            print("Has ganado el juego.")
        else:
            print("La máquina ha ganado el juego.")

    def menu(self):
        try:
            while True:
                print("*************************************************")
                print("1. Jugar a Piedra, Papel, Tijera, Lagarto, Spock")
                print("2. Salir")
                print("*************************************************")
                
                opcion = input("Elige una opción (1 o 2): ")

                if opcion == "1":
                    self.jugar(self)
                elif opcion == "2":
                    print("Saliendo del juego.")
                    break
                else:
                    print("Opción no válida. Por favor, elige 1 o 2.\n")
        except:
            print("\n-----------------------------------------------------")
            print("Error el main principal del juego, salimos al menu")
            print("-----------------------------------------------------")
