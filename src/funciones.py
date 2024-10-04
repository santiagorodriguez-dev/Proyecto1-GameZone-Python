class Mascota:
    def __init__(self, color, especie, tamanio, edad, raza = None):
        self.color = color
        self.especie = especie
        self.tamanio = tamanio
        self.edad = edad
        self.raza = raza
    
    def cumple(self):
        self.edad = self.edad + 1
        return self.edad
    
    def vacunas(self, numero_de_vacunas):
        self.numero_de_vacunas = numero_de_vacunas

        if self.especie == 'gato':
            if numero_de_vacunas < 3:
                print("deberias ponerles todas las vacunas")
            else:
                print("esta vacunado")

class Gatos(Mascota):
    def __init__(self, color, especie, tamanio, edad, raza, arena):
        self.arena = arena
        super().__init__(color, especie, tamanio, edad, raza)
    
    def funcion_gato(self):
        print(self.edad)