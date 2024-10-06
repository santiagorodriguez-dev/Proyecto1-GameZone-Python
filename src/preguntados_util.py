
import ast
import random

"""
    Clase que proporciona utilidades para el juego de Preguntados.

    Atributos:
        categorias (list): Lista de categorías disponibles para las preguntas.
        num_preguntas (int): Número total de preguntas a seleccionar para el juego.
        num_para_victorias (int): Número de respuestas correctas necesarias para ganar.

    Métodos:
        read_data_file() -> dict:
            Lee el archivo de datos y devuelve un diccionario con las preguntas.

        todas_las_preguntas(input_data: dict, categorias: list) -> list:
            Extrae todas las preguntas de las categorías proporcionadas en input_data.
            Parámetros:
                input_data (dict): Diccionario que contiene preguntas organizadas por categorías.
                categorias (list): Lista de categorías de las que extraer las preguntas.
        
        list_random_preguntas(list_preguntas: list, num_random: int) -> list:
            Selecciona un número aleatorio de preguntas de la lista proporcionada.
            Parámetros:
                list_preguntas (list): Lista de preguntas de las cuales seleccionar.
                num_random (int): Número de preguntas a seleccionar aleatoriamente.
        
        extrae_respuestas_pregunta(pregunta: dict) -> list:
            Extrae las respuestas de una pregunta dada y devuelve una lista de tuplas (respuesta, es_correcta).
            Parámetros:
                pregunta (dict): Pregunta de la cual extraer las respuestas.

        input_data_valida() -> str:
            Captura y valida la respuesta del usuario, retornando 'a', 'b', 'c', 'd' o 'z' si es inválida.
        
        mostrar_menu() -> None:
            Muestra el menú principal del juego en la consola.
"""

class PreguntadosUtil:

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
        print("2. Salir al menu principal de juegos")
        print("*************************")