import random

def main():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número entre 1 y 100: '))
    while numero_aleatorio != numero_elegido:
        if numero_aleatorio < numero_elegido:
            print('Elige un número menor')
        else:
            print('Elige un número mayor')
        numero_elegido = int(input('Elige otro número: '))
    print('¡¡ Acertaste !!')

if __name__ == '__main__':
    main()
