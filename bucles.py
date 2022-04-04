def main():
    
    base = 2
    exponente = 1
    potencia = 2
    LIMITE = 1000

    while potencia < LIMITE:
        potencia = base ** exponente
        print(f"{base} elevado a {exponente} es igual a {potencia}")
        exponente += 1


if __name__ == '__main__':
    main()