import random

"""
    Clase utilitaria para gestionar las reglas y las elecciones del juego Piedra, Papel, Tijera, Lagarto, Spock.

    Métodos:
        eleccion_maquina(): Devuelve una opción aleatoria seleccionada por la máquina.
        determinar_ganador(jugador_humano, maquina): Determina el ganador en función de las elecciones del jugador y la máquina.
"""

class PiedraPapelTijeraLagartoSpockUtil:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

        self.reglas = {
            "piedra": ["tijera", "lagarto"],
            "papel": ["piedra", "spock"],
            "tijera": ["papel", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tijera", "piedra"]
        }

    def eleccion_maquina(self):
        return random.choice(self.opciones)

    def determinar_ganador(self, jugador_humano, maquina):
        if jugador_humano == maquina:
            return "Empate"
        elif maquina in self.reglas[jugador_humano]:
            return "Jugador"
        else:
            return "Maquina"
