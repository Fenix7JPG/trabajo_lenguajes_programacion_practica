class Persona:
    # El constructor inicializa los datos de la persona
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

    # Método para que la persona realice una acción
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
