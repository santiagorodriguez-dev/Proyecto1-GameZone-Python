import random

class Ahorcado:
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

