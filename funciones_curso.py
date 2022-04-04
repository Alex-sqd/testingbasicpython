
# Definiendo una sencilla función
# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones')
#
#
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# Esto hace lo mismo que lo anterior pero más engorroso:
# print('Mensaje especial: ')
# print('¡Estoy aprendiendo a usar funciones')
# print('Mensaje especial: ')
# print('¡Estoy aprendiendo a usar funciones')
# print('Mensaje especial: ')
# print('¡Estoy aprendiendo a usar funciones')

def conversacion(mensaje):
    print('Hola')
    print('¿Cómo estás?')
    print(f'Elegiste la opción {mensaje}')
    print('Adiós')


opcion = input('Elige una opción: ')

if opcion in ('1','2','3'):
    conversacion(opcion)
else:
    print('Escribe una opción correcta')


# Esto hace lo mismo que la función conversacion()
# if opcion == '1':
#     print('Hola')
#     print('¿Cómo estás?')
#     print('Elegiste la opción 1')
#     print('Adiós')
# elif opcion == '2':
#     print('Hola')
#     print('¿Cómo estás?')
#     print('Elegiste la opción 2')
#     print('Adiós')
# elif opcion == '3':
#     print('Hola')
#     print('¿Cómo estás?')
#     print('Elegiste la opción 3')
#     print('Adiós')
# else:
#     print('Escribe una opción correcta')