"""Crear un programa en el que se utilicen
los diferentes tipos de bucles e interrupciones
"""

def main():
    
    texto = input('Escribe un texto: ')
    espacio = 0

    for caracter in texto:
        if caracter == ' ':
            espacio += 1
        elif caracter == ',':
            print('Contiene una coma. No puede contener comas')
            break
        else:
            print(caracter)

    print(f"Número de espacios = {espacio}")
    

if __name__ == '__main__':
    main()