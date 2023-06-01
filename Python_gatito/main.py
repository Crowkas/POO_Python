from gatito import Gatito
from gatito_siames import GatitoSiames
from gatito_persa import GatitoPersa

# Creación de objetos utilizando el método constructor
gatito1 = Gatito("Pelusa", 2, "blanco")  # Creación de objeto: gatito1
gatito1.presentarse()  # Llamada al método presentarse del gatito3
gatito1.maullar()  # Llamada al método maullar del gatito1

gatito2 = GatitoSiames("Mimi", 3, "marrón", "ojos azules")  # Creación de objeto: gatito2 (clase hija)
gatito2.presentarse()  # Llamada al método presentarse del gatito3
gatito2.maullar()  # Llamada al método maullar del gatito2

gatito3 = GatitoPersa("Luna", 1, "gris")  # Creación de objeto: gatito3 (clase hija)
gatito3.presentarse()  # Llamada al método presentarse del gatito3
gatito3.maullar()  # Llamada al método maullar del gatito3

'''
Encapsulamiento: Las propiedades nombre, edad y color están encapsuladas dentro de la clase Gatito. 
Estas propiedades solo son accesibles a través de los métodos de la clase.

Abstracción: La clase Gatito es una abstracción que representa las características comunes de un gatito. 
Las clases hijas, GatitoSiames y GatitoPersa, son abstracciones más específicas que heredan las propiedades 
y métodos de la clase padre.

Herencia: Las clases GatitoSiames y GatitoPersa heredan de la clase Gatito. 
Esto significa que las clases hijas heredan las propiedades y métodos de la clase padre. 
En el ejemplo, las clases hijas sobrescriben el método presentarse() para añadir comportamiento específico.

Polimorfismo: Las clases GatitoSiames y GatitoPersa tienen el método presentarse(), 
que es una forma polimórfica del método en la clase padre Gatito. 
Cada clase hija implementa el método de manera diferente, mostrando su propia presentación.

En resumen, el ejemplo ilustra el uso de encapsulamiento, abstracción, herencia y polimorfismo en el contexto de la programación orientada a objetos con gatitos como objeto de estudio.'''