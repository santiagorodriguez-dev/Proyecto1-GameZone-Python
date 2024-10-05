
import ast
import random

class Preguntados_Support:

    categorias = ["Cultura General", "Historia", "Entretenimiento", "Ciencia"]

    def read_data_file(self):

        with open('./src/datos.txt', 'r',-1,"utf-8") as archivo:
            contenido = archivo.read()
            return ast.literal_eval(contenido)
    
    def todas_las_preguntas(self, input_data, categorias):

        preguntas = []

        for categoria in categorias:
            if (input_data.get(categoria)) != None:
                for pregunta in input_data.get(categoria):
                    preguntas.append(pregunta)

        return preguntas
    
    def list_random_preguntas(self, list_preguntas,num_random):
        return random.choices(list_preguntas,k=num_random)
    
    def extrae_respuestas_pregunta(self, pregunta):

        result = []

        for clave, valor in pregunta.items():
            if(isinstance(valor, dict)):
                for clave_sub, valor_sub in valor.items():
                    result.append((clave_sub,valor_sub))

        return result
    
    def input_data(self):
        dato = input()
        if dato == 'a' or dato == 'b' or dato == 'c' or  dato == 'd':
            return dato
        else:
            return 'z'