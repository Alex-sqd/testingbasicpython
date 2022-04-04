import random

def main():

    def acierto(numero_secreto):
        numero = int(input('Elige un número: '))
        if numero >= 0 and numero <= 100:
            if numero > numero_secreto:
                print ('El número elegido es mayor')
                return False
            elif numero < numero_secreto:
                print('El número elegido es menor')
                return False
            else:
                print('¡¡ Acertaste !!')
                return True
        else:
            print('El número no es válido')
            return False
        
    numero_secreto = random.randint(0, 100)
    
    while acierto(numero_secreto) == False:
        acierto(numero_secreto)

        
if __name__ == '__main__':
    main()