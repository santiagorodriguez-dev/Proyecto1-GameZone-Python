from src.support_preguntados import Preguntados_Support as pre_supp

class Preguntados:

    def __init__(self, salida):
        self.salida = salida

    def inicio_preguntados(self):

        self.salida = False

        def menu():
            while True:
                pre_supp.mostrar_menu(pre_supp)
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
            lista_preguntas_con_categorias = pre_supp.read_data_file(pre_supp)
            lista_todas_preguntas = pre_supp.todas_las_preguntas(pre_supp,lista_preguntas_con_categorias,pre_supp.categorias)
            lista_preguntas_aletorias = pre_supp.list_random_preguntas(pre_supp,lista_todas_preguntas,pre_supp.num_preguntas)
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
                    respuestas = pre_supp.extrae_respuestas_pregunta(pre_supp,pregunta)
                    
                    for pre,resp in respuestas:
                        print(pre)

                    print("------------------------------------------------------------------")
                    print("\n")
                    resp_usuario = pre_supp.input_data_valida(pre_supp)
                    if resp_usuario != 'z':
                            for r,v in respuestas:
                                if r[:1] == resp_usuario and v is True:
                                    print("Has Acertado")
                                    contador_aciertos = contador_aciertos  + 1
                                    if (contador_aciertos == pre_supp.num_para_victorias):
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
        
     



