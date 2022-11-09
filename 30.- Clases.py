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
    
persona1 = Persona("Nicolas", 30)
print(persona1)
print(len(persona1))
persona1.hablar("Hola mundo")

persona2 = Persona("Maria", 20)
persona2.hablar("Este es otro mensaje")
print(persona2.edad)


# Herencia
class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + " Sueldo: " + str(self.sueldo)

    def hablar(self, mensaje):
        return super().hablar(mensaje)

empleado1 = Empleado("Miguel", 25, 100)
print(empleado1)
empleado1.hablar("Otro mensaje")
print(empleado1.nombre + str(empleado1.edad) + str(empleado1.sueldo))
