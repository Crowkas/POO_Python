from gatito import Gatito

class GatitoSiames(Gatito):
    def __init__(self, nombre, edad, color, rasgo):
        super().__init__(nombre, edad, color)
        self.rasgo = rasgo  # Atributo específico de la subclase GatitoSiames

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, mi color es {self.color}, tengo {self.rasgo} y soy un gatito siamés")
        # Método: presentarse del gatito siamés

    def maullar(self):
        print("Prrr")  # Método: maullar del gatito siames   