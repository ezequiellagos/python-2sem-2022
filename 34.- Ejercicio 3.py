# Cree una calculadora que reciba una lista de numeros. Utilice función lambda, map, filter o reduce según corresponda. Imprima el resultado por la consola. 

# Por ejemplo, si la lista es [2, 3, 4, 5, 6], el programa debe devolver:
# Suma: 20
# Resta: -16
# Multiplicación: 720
# División: 0.001388888888888889
# Exponente: 2348542582773833227889480596789337027375682548908319870707290971532209025114608443463698998384768703031934976
# Raiz cuadrada: 1.001927263624698

from functools import reduce

def suma(lista):
    return reduce(lambda x, y: x + y, lista)

def resta(lista):
    return reduce(lambda x, y: x - y, lista)

def multiplicacion(lista):
    return reduce(lambda x, y: x * y, lista)

def division(lista):
    return reduce(lambda x, y: x / y, lista)

def exponente(lista):
    return reduce(lambda x, y: x ** y, lista)

def raiz_cuadrada(lista):
    return reduce(lambda x, y: x ** (1 / y), lista)

def main():
    lista = [2, 3, 4, 5, 6]
    print(f"Suma: {suma(lista)}")
    print(f"Resta: {resta(lista)}")
    print(f"Multiplicación: {multiplicacion(lista)}")
    print(f"División: {division(lista)}")
    print(f"Exponente: {exponente(lista)}")
    print(f"Raiz cuadrada: {raiz_cuadrada(lista)}")

if __name__ == '__main__':
    main()