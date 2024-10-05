from src.preguntados import Preguntados as pre
from src.tres_en_raya import Tres_En_Raya as tres

def main():
   pre.salida = False
   tres.salida = False
   #pre.inicio_preguntados(pre)
   tres.tres_en_raya(tres)
   print (pre.salida)
   print (tres.salida)

if __name__ == "__main__":
   main()

# funcion mostrar menu

# funcion main
#while true
