# Cree una función que determine si un numero es primo o no. Calcule los numeros primos del 1 al 1000. Solo la función para determinar que es primo puede llevar un for, el resto debe ser con lambda, map, filter o reduce. Imprima la lista por la consola.

def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def main():
    lista_numeros = range(1, 1000)
    lista_primos = list(filter(es_primo, lista_numeros))

    print(lista_primos)

if __name__ == '__main__':
    main()