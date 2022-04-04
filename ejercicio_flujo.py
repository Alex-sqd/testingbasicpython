numero = int(input("Dime un número entero: "))
operador = int(input("Dime otro número entero: "))

if numero > operador:
    print(f"La suma es: {numero+operador}")
elif operador > numero:
    print(f"La diferencia es: {operador-numero}")
else:
    print(f"La potencia es: {numero**operador}")