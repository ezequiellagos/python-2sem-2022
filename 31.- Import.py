# Import

# from nombre_libreria import nombre_de_la_clase
# from nombre_libreria import *
# import nombre_libreria
# from nombre_libreria import nombre_de_la_clase as nombre_alias

from clases import Persona
# import math

persona = Persona("Diego", 27)
print(persona)



from clases import Persona as P

persona2 = P("Ezequiel", 10)
print(persona2)