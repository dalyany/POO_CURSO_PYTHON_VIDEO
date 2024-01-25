# Definición de la clase Estudiante
class Estudiante:
    # Atributos: nombre, edad, nivel

    # Constructor de la clase
    def __init__(self, nombre, edad, nivel):
        self.nombre = nombre  # Inicialización del atributo nombre con el valor proporcionado
        self.edad = edad      # Inicialización del atributo edad con el valor proporcionado
        self.nivel = nivel    # Inicialización del atributo nivel con el valor proporcionado

    # Método estudiar
    def estudiar(self):
        # Retornar una cadena con un mensaje que hace referencia al nombre del estudiante y su nivel
        return f'\nEl estudiante {self.nombre} está estudiando en el nivel {self.nivel}\n'

    # Método cumplir_anios
    def cumplir_anios(self):
        # Incrementar la edad del estudiante y retornar un mensaje indicando el cambio
        self.edad += 1
        return f'\n¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.\n'

# Solicitar al usuario ingresar el nombre del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")

# Solicitar al usuario ingresar la edad del estudiante y convertir el input a un entero
edad_estudiante = int(input("Ingrese la edad del estudiante: "))

# Solicitar al usuario ingresar el nivel del estudiante y asignarlo a la variable nivel_estudiante
nivel_estudiante = input("Ingrese el nivel del estudiante 'GRADO' al que pertenece: ")

# Crear una instancia de la clase Estudiante con los datos proporcionados por el usuario
estudiante1 = Estudiante(nombre_estudiante, edad_estudiante, nivel_estudiante)

# Llamar al método estudiar de la instancia de la clase Estudiante e imprimir el resultado
print(estudiante1.estudiar())

# Llamar al método cumplir_anios de la instancia de la clase Estudiante e imprimir el resultado
print(estudiante1.cumplir_anios())
