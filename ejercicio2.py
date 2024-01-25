# Definición de la clase Persona
class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo: nombre
        self.edad = edad      # Atributo: edad

    # Método para imprimir datos
    def imprimirDatos(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'

# Aplicamos herencia -> Estudiante hereda de Persona los atributos
class Estudiante(Persona):
    # Constructor
    def __init__(self, nombre, edad, grado):
        # Llamamos al constructor de la clase padre (Persona) y heredamos atributos nombre y edad
        super().__init__(nombre, edad)
        self.grado = grado  # Nuevo atributo: grado

    # Método para imprimir datos del estudiante, incluyendo el grado
    def imprimirGrado(self):
        return f'{self.imprimirDatos()}\nGrado cursando: {self.grado}'

# Crear una instancia de la clase Persona
nombre_persona = input('Ingresar nombre de la persona: ')
edad_persona = int(input('Ingresar edad de la persona: '))
persona1 = Persona(nombre_persona, edad_persona)

# Imprimir datos de la persona utilizando el método imprimirDatos
print('DATOS DE LA PERSONA:\n')
print(persona1.imprimirDatos())

# Crear una instancia de la clase Estudiante
nombre_estudiante = input('Ingresar nombre del estudiante: ')
edad_estudiante = int(input('Ingresar edad del estudiante: '))
grado_estudiante = input('Ingrese un grado del estudiante: ')
estudiante1 = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante)

# Imprimir datos del estudiante, incluyendo el grado, utilizando el método imprimirGrado
print('DATOS DEL ESTUDIANTE:\n')
print(estudiante1.imprimirGrado())
