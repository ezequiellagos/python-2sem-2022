# Clases

class Persona:
    
    # Constructor
    # se ejecuta una sola vez
    # self, es el equivalente al this en java
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad)

    def __len__(self):
        return self.edad
    
    def __del__(self):
        print("Se ha eliminado la persona")

    # Metodo
    def hablar(self, mensaje):
        print(self.nombre + ": " + mensaje)
    


# Herencia
class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + " Sueldo: " + str(self.sueldo)

    def hablar(self, mensaje):
        return super().hablar(mensaje)

