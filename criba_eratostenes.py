# La criba de Eratóstenes
"""
La criba de Eratóstenes es un algoritmo para obtener los números primos por debajo
de un número determinado.

 Necesitamos un número por debajo del cual obtener los números primos.
 Primero se eliminan todos los números pares.
 Después uno a uno se van comprobando los cuadrados de los números primos:
    Si el cuadrado de 3 es menor que el número se eliminan todos los múltiplos de 3.
    Si el cuadrado de 5 es menor que el número se eliminan todos los múltiplos de 5.
    Si el cuadrado es 7 es menor que el número se eliminan todos los múltiplos de 7.
    Así sucesivamente hasta llegar a un número primo cuyo cuadrado sea mayor que el número dado.

    El inconveniente es que requiere conocer todos los números primos hasta llegar a la raiz cuadrada
    del número dado. Tales números primos pueden obtenerse de la "Prueba de Primalidad".

Es un reto interesante para un momento en que se controle mejor el lenguaje. Es una buena práctica para
el dominio de las listas.
"""
def main():
    pass


if __name__ == '__main__':
    main()
