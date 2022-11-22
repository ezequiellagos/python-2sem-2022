# Pregunte al usuario sus colores favoritos, cuando el usuario ingrese "salir" el programa debe terminar de pedir sus colores favoritos. Cree una función que imprima en mayúsculas los colores, uno por linea. Utilice kwargs o args según corresponda.

def imprimir_color(*args):
    print("Sus colores favoritos son:")
    for color in args:
        print(color)

def main():
    colores = []
    while True:
        color = input("Ingrese un color favorito: ")
        if color == "salir":
            break
        colores.append(color.upper())
    imprimir_color(*colores)

if __name__ == '__main__':
    main()