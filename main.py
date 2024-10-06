from src.preguntados import Preguntados as pre
from src.tres_en_raya import TresEnRaya as tres
from src.ahorcados import AhorcadoMain as ahc
from src.piedra_papel_tijera_lagarto_pock import PiedraPapelTijeraLagartoSpock as pie

def mostrar_menu():
        try:
            while True:
                print("\n***********************************************")
                print("** MENÚ PRINCIPAL *****************************")
                print("***********************************************")
                print("1. Jugar Preguntados")
                print("2. Jugar Tres en Raya")
                print("3. Jugar Ahorcado")
                print("4. Jugar Piedra, Papel, Tijera, Lagarto, Spock")
                print("5. Salir")
                print("***********************************************")

                opcion = input("Elige una opción (1-5): ")

                if opcion == "1":
                    pre.inicio_preguntados(pre)
                elif opcion == "2":
                    tres.tres_en_raya(tres)
                elif opcion == "3":
                     ahc.menu(ahc)
                elif opcion == "4":
                     pie.menu(pie)
                elif opcion == "5":
                    print("Saliendo del Menu. Chau")
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción entre 1 y 5.\n")
        except:
            print("\n------------------------------------------------------------")
            print("Error el main principal, fin menu, vuelva a cargar el programa")
            print("------------------------------------------------------------")

def main():
   mostrar_menu()
   
if __name__ == "__main__":
   main()
