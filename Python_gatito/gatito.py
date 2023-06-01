class Gatito:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre  # Propiedad: nombre del gatito
        self.edad = edad  # Propiedad: edad del gatito
        self.color = color  # Propiedad: color del gatito

    def maullar(self):
        print("Miau")  # Método: maullar del gatito

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y mi color es {self.color}")
        # Método: presentarse del gatito