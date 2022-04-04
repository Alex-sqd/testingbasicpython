def main():
    texto = input('Escribe un texto: ')

    for caracter in texto:
        if caracter == 'o':
            break
        print(caracter)


if __name__ == '__main__':
    main()