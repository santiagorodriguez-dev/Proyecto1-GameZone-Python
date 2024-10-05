
import ast
import random

class Preguntados_Support:

    categorias = ["Cultura General", "Historia", "Entretenimiento", "Ciencia"]
    num_preguntas = 10
    num_para_victorias = 10

    def read_data_file(self):
        try:
            with open('./src/datos.txt', 'r',-1,"utf-8") as archivo:
                contenido = archivo.read()
                return ast.literal_eval(contenido)
        except:
            print("Error al abrir el fichero con los datos de las preguntas")
    
    def todas_las_preguntas(self, input_data, categorias):
        try:
            preguntas = []

            for categoria in categorias:
                if (input_data.get(categoria)) != None:
                    for pregunta in input_data.get(categoria):
                        preguntas.append(pregunta)

            return preguntas
        except:
            print("Error al extraer todas las preguntas")
    
    def list_random_preguntas(self, list_preguntas,num_random):
        try:
            return random.choices(list_preguntas,k=num_random)
        except:
            print("Error al sacar la lista random de preguntas")
    
    def extrae_respuestas_pregunta(self, pregunta):
        try:
            result = []
            for clave, valor in pregunta.items():
                if(isinstance(valor, dict)):
                    for clave_sub, valor_sub in valor.items():
                        result.append((clave_sub,valor_sub))

            return result
        except:
            print("Error al extraer las respuestas de las pregunta")
    
    def input_data_valida(self):
        try:
            dato = input()
            dato = dato.lower()
            if dato == 'a' or dato == 'b' or dato == 'c' or  dato == 'd':
                return dato
            else:
                return 'z'
        except:
            print("Error al capturar y validar la respuesta de la pregunta")
        

    def mostrar_menu(self):
        print("*************************")
        print("**  JUEGO APALABRADOS  **")
        print("*************************")
        print("1. Jugar")
        print("2. Salir")
        print("*************************")