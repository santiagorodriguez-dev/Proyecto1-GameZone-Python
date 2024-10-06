from src.ahorcadoUtil import AhorcadoUtil

class AhorcadoMain:

    def __init__(self, salida):
        self.salida = salida

    def jugar(self):
        try:
            palabras = ["paella", "tapas", "gazpacho", "churros", "pisto", "tortilla", "cocido", "pulpo", "fabada", "bacalao"]

            juego = AhorcadoUtil(palabras,6)

            print("\n¡Empezamos!")
            print("\nPista: todas las palabras son comidas de españa ;)")
            
            while not juego.ha_ganado() and not juego.intentos == 0:
                print("\nPalabra: ", juego.mostrar_progreso())  
                print(f"Intentos restantes: {juego.intentos}")
                juego.mostrar_ahorcado()

                letra = input("Adivina una letra: ").strip().upper()

                if len(letra) != 1 or not letra.isalpha():
                    print("Ingresa solo una letra válida.")
                    continue

                if juego.adivinar_letra(letra):
                    print(f"¡Bien hecho! '{letra}' está en la palabra.")
                else:
                    print(f"La letra, '{letra}' no está , o ya la has introducido")

            if juego.ha_ganado():
                print(f"¡Ganaste! La palabra era: {juego.palabra_secreta}")
            else:
                juego.mostrar_ahorcado()
                print(f"Perdiste. La palabra era: {juego.palabra_secreta}")

        except:
            print("\n-----------------------------------------------------")
            print("Error el main principal del juego, salimos al menu")
            print("-----------------------------------------------------")
            
    def menu(self):
        try:
            while True:
                print("\n--- Ahorcado ---")
                print("1. Jugar")
                print("2. Salir")

                opcion = input("Elige una opción: ")

                if opcion == '1':
                    self.jugar(self)
                elif opcion == '2':
                    print("Hasta Pronto")
                    break
                else:
                    print("Opción no válida. Por favor elige 1 o 2.")

        except:
            print("\n--------------------------------------------------------------------")
            print("Error el menu del juego volvemos al menu principal de todos los juegos")
            print("--------------------------------------------------------------------")
