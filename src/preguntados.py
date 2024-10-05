from src.support_preguntados import Preguntados_Support as pre_supp

class Preguntados:

    def inicio_preguntados(self):
        todas_preguntas_categorias = pre_supp.read_data_file(pre_supp)
        lista_preguntas = pre_supp.todas_las_preguntas(pre_supp,todas_preguntas_categorias,pre_supp.categorias)
        resultado = pre_supp.list_random_preguntas(pre_supp,lista_preguntas,pre_supp.num_preguntas)

        print(resultado)

