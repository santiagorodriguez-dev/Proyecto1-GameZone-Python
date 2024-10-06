from src.preguntados_util import PreguntadosUtil as pre_util

"""
    Clase principal para el juego de Preguntados.

    Esta clase gestiona el flujo del juego, incluyendo la visualización del menú, 
    la selección y presentación de preguntas, así como la verificación de respuestas del usuario.

    Atributos:
        salida (bool): Indica si se debe salir del juego.

    Métodos:
        inicio_preguntados(): Inicia el juego, mostrando el menú y gestionando la lógica de juego.
"""

class Preguntados:

    def __init__(self, salida):
        self.salida = salida

    def inicio_preguntados(self):  
        def menu():
            while True:
                pre_util.mostrar_menu(pre_util)
                opcion = input("Elige una opción (1-2): ")
                if opcion == '1':
                    jugar()
                elif opcion == '2':
                    salir()
                    break
                else:
                    print("\nOpción no válida. Elige una opción entre 1 y 2.\n")

        def jugar():
            # INI Cargamos datos
            lista_preguntas_con_categorias = pre_util.read_data_file(pre_util)
            lista_todas_preguntas = pre_util.todas_las_preguntas(pre_util,lista_preguntas_con_categorias,pre_util.categorias)
            lista_preguntas_aletorias = pre_util.list_random_preguntas(pre_util,lista_todas_preguntas,pre_util.num_preguntas)
            # FIN Cargamos datos

            contador_aciertos = 0
            salir_de_partida = False

            for pregunta in lista_preguntas_aletorias:
                if salir_de_partida == True:
                    break
                else:
                    print("\n")
                    print("------------------------------------------------------------------")
                    print(f"Respuestas acertadas: {contador_aciertos}")
                    print(pregunta.get('Pregunta'))
                    respuestas = pre_util.extrae_respuestas_pregunta(pre_util,pregunta)
                    
                    for pre,resp in respuestas:
                        print(pre)

                    print("------------------------------------------------------------------")
                    print("\n")
                    resp_usuario = pre_util.input_data_valida(pre_util)
                    if resp_usuario != 'z':
                            for r,v in respuestas:
                                if r[:1] == resp_usuario and v is True:
                                    print("Has Acertado")
                                    contador_aciertos = contador_aciertos  + 1
                                    if (contador_aciertos == pre_util.num_para_victorias):
                                        salir_de_partida = True
                                        print("\n")
                                        print("Has Ganado!!!")
                                        print("\n")
                                    break
                                else:
                                    print("\n")
                                    print("La respuesta no es correta")
                                    print("\n")
                                    salir_de_partida = True
                                    break
                    else:
                        print("\n")
                        print("Opcion incorrecta has perdido")
                        print("\n")
                        salir_de_partida = True
                        break

        def salir():
            self.salida = True

        #cargamos el menu del juego
        menu()
        
     



