from abc import ABC, abstractmethod

# Definición de la clase Animal como clase abstracta
class Animal(ABC):
    # Constructor
    def __init__(self, nombre, edad, especie, colorDominante):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.colorDominante = colorDominante
    
    @abstractmethod
    def decirInfo(self):
        pass
    
    def comer(self):
        pass

# Clase Mamifero que hereda de la clase Animal
class Mamifero(Animal):
    # Constructor
    def __init__(self, nombre, edad, especie, colorDominante):
        # Llamamos al constructor de la clase padre (Animal) y heredamos sus atributos
        super().__init__(nombre, edad, especie, colorDominante)
        
    # Método para imprimir información específica de un mamífero
    def decirInfo(self):
        return f"Soy un mamífero llamado {self.nombre}, tengo {self.edad} años."

    # Método específico de los mamíferos
    def amamantar(self):
        return '\nEstoy amamantando a mi cría\n'

# Clase Ave que hereda de la clase Animal
class Ave(Animal):
    # Constructor
    def __init__(self, nombre, edad, especie, colorDominante):
        # Llamamos al constructor de la clase padre (Animal) y heredamos sus atributos
        super().__init__(nombre, edad, especie, colorDominante)
    
    # Método para imprimir información específica de un ave
    def decirInfo(self):
        return f"Soy un ave llamada {self.nombre}, tengo {self.edad} años."

    # Método específico de las aves
    def volar(self):
        return '\nVolando alto con mis alas\n'

# Clase Murcielago que hereda de las clases Mamifero y Ave
class Murcielago(Mamifero, Ave):
    # Constructor
    def __init__(self, nombre, edad, especie, colorDominante):
        # Llamamos al constructor de la clase padre (Mamifero) y heredamos sus atributos
        super().__init__(nombre, edad, especie, colorDominante)
    
    # Método para imprimir información específica de un murciélago
    def decirInfo(self):
        return f"Soy un murciélago llamado {self.nombre}, tengo {self.edad} años."

# Crear una instancia de la clase Murcielago
murcielago = Murcielago('Gerald', 2, 'Murciélago', 'Negro')

# Imprimir acciones específicas del murciélago
print('MURCIÉLAGO: ACCIONES ESPECÍFICAS\n')
print(murcielago.amamantar())
print(murcielago.volar())

# Imprimir información general del murciélago utilizando el método decirInfo
print('MURCIÉLAGO: INFORMACIÓN GENERAL\n')
print(murcielago.decirInfo())
