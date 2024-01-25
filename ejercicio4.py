class Personaje:
    # Constructor Personaje 
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    # Método para representar el objeto como cadena
    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'

    # Método para sumar dos personajes y crear un nuevo personaje
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza) / 2) ** 2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad) / 2) ** 2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

    # Método para comparar la fuerza de dos personajes
    def comparar_fuerza(self, otro_pj):
        if self.fuerza > otro_pj.fuerza:
            return f"{self.nombre} es más fuerte que {otro_pj.nombre}."
        elif self.fuerza < otro_pj.fuerza:
            return f"{otro_pj.nombre} es más fuerte que {self.nombre}."
        else:
            return f"{self.nombre} y {otro_pj.nombre} tienen la misma fuerza."

    # Método para aumentar la velocidad del personaje
    def aumentar_velocidad(self, aumento):
        self.velocidad += aumento
        return f"{self.nombre} ha aumentado su velocidad en {aumento} unidades."

# Crear instancias de la clase Personaje
goku = Personaje("Goku", 100, 1901)
vegeta = Personaje("Vegeta", 99, 99)
jiren = Personaje("Jiren", 125, 122)

# Sumar dos personajes para crear un nuevo personaje
gogeta = goku + vegeta

# Imprimir fuerza y velocidad del personaje resultante
print("Fuerza de Gogeta:", gogeta.fuerza)
print("Velocidad de Gogeta:", gogeta.velocidad)

# Comparar fuerza entre personajes
print(gogeta.comparar_fuerza(jiren))

# Aumentar velocidad de un personaje
print(gogeta.aumentar_velocidad(50))
