import random

"""
    Clase que gestiona la lógica del juego del Ahorcado.

    Esta clase se encarga de seleccionar una palabra secreta, realizar el seguimiento de los intentos del jugador,
    y gestionar las letras adivinadas, además de proporcionar funciones para mostrar el progreso del juego 
    y los estados del ahorcado.

    Atributos:
        palabra_secreta (str): La palabra que el jugador debe adivinar.
        intentos (int): Número de intentos permitidos para adivinar la palabra.
        letras_adivinadas (list): Lista de letras que el jugador ya ha adivinado.
        estado_palabra_adivinar (list): Estado actual de la palabra a adivinar, mostrando letras adivinadas y guiones bajos.

    Métodos:
        adivinar_letra(letra): Procesa la letra adivinada por el jugador y actualiza el estado del juego.
        mostrar_progreso(): Devuelve una representación visual del progreso actual del juego.
        ha_ganado(): Verifica si el jugador ha adivinado todas las letras de la palabra.
        ha_perdido(): Verifica si el jugador ha agotado sus intentos.
        mostrar_ahorcado(): Muestra el estado actual del ahorcado basado en los intentos restantes.
"""

class AhorcadoUtil:
    def __init__(self, palabras, intentos):
        self.palabra_secreta = random.choice(palabras).upper()
        self.intentos = intentos
        self.letras_adivinadas = []
        self.estado_palabra_adivinar = ["_"] * len(self.palabra_secreta)

    def adivinar_letra(self, letra):
        letra = letra.upper() 

        if letra in self.letras_adivinadas:
            return False

        self.letras_adivinadas.append(letra)

        # recorremos la letras de la palabra secreta, si la encuentra, añadimos
        # a la posicion en la que esta en estado_palabra_adivinar y asi poder mostrarla despues
        if letra in self.palabra_secreta:
            for i, l in enumerate(self.palabra_secreta):
                if l == letra:
                    self.estado_palabra_adivinar[i] = letra 
            return True
        else:
            self.intentos -= 1
            return False

    def mostrar_progreso(self):
        return " ".join(self.estado_palabra_adivinar)

    def ha_ganado(self):
        if "_" in self.estado_palabra_adivinar:
            return False
        else:
            return True

    def ha_perdido(self):
        if self.intentos == 0:
            return True
        else:
            return False

    def mostrar_ahorcado(self):
        dibujo_estados = [
            """
               _______
               |     |
               |    
               |
               |
               |
            -------
            """,
            """
               _______
               |     |
               |     O
               |
               |
               |
            -------
            """,
            """
               _______
               |     |
               |     O
               |     |
               |
               |
            -------
            """,
            """
               _______
               |     |
               |     O
               |    /|
               |
               |
            -------
            """,
            """
               _______
               |     |
               |     O
               |    /|\\
               |
               |
            -------
            """,
            """
               _______
               |     |
               |     O
               |    /|\\
               |    / 
               |
            -------
            """,
            """
               _______
               |     |
               |     O
               |    /|\\
               |    / \\
               |
            -------
            """
        ]
        print(dibujo_estados[6 - self.intentos])

