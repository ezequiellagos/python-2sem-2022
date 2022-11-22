# Resuelva los siguientes bloques de código añadiendo las sentencias Try que considere necesario. Si el bloque de código no tiene errores, imprima "El bloque de código no tiene errores" en la consola y el resultado del bloque según corresponda. Si el bloque de código tiene errores, imprima el error en la consola.

def bloque_1():
    mi_lista = ["Python","C","C++","JavaScript"]
    try:
        print(mi_lista[5])
    except IndexError as error:
        print("Error, el indice no existe")
        print(error)
    else:
        print("El bloque de código no tiene errores")

def bloque_2(num):
    try:
        resultado = num + 10
    except TypeError as error:
        print("Error, el valor no es un numero")
        print(error)
    else:
        print(resultado)
        print("El bloque de código no tiene errores")

def bloque_3():
    capitales  = {
        "Colombia": "Bogotá",
        "Argentina": "Buenos Aires",
        "Perú": "Lima",
        "Chile": "Santiago de Chile",
    }
    try:
        print(capitales["Brasil"])
    except KeyError as error:
        print("Error, la llave no existe")
        print(error)
    else:
        print("El bloque de código no tiene errores")

        

def main():
    # Esta función no debe ser modificada. Modifique las funciones bloque_1, bloque_2, bloque_3 y bloque_4.
    # Si modifica esta sección para hacer pruebas recuerde cambiarla antes de enviar el ejercicio.
    print("Bloque 1")
    bloque_1()
    print("-------------")

    print("Bloque 2")
    bloque_2("dos")
    print("-------------")

    print("Bloque 3")
    bloque_3()
    print("-------------")

if __name__ == '__main__':
    main()












def bloque_1():
    mi_lista = ["Python","C","C++","JavaScript"]
    print(mi_lista[5])

def bloque_2(num):
    resultado = num + 10
    print(resultado)

def bloque_3():
    capitales  = {
        "Colombia": "Bogotá",
        "Argentina": "Buenos Aires",
        "Perú": "Lima",
        "Chile": "Santiago de Chile",
    }
    print(capitales["Brasil"])
    