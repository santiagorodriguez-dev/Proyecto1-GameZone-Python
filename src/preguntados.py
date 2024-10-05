from src.support_preguntados import Preguntados_Support as pgm_sup

class Preguntados:

    def inicio_preguntados(self):
        todas_preguntas_categorias = pgm_sup.read_data_file(pgm_sup)
        lista_preguntas = pgm_sup.todas_las_preguntas(pgm_sup,todas_preguntas_categorias,pgm_sup.categorias)
        resultado = pgm_sup.list_random_preguntas(pgm_sup,lista_preguntas,10)

        print(resultado)

