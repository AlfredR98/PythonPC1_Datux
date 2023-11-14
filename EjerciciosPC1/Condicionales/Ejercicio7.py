'''Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
# - Mostrar una suma de los dos números
# - Mostrar una resta de los dos números (el primero menos el segundo)
# - Mostrar una multiplicación de los dos números
# - En caso de introducir una opción inválida, el programa informará de que no es correcta.'''

n1 = int(input('Ingrese el primer número:\n'))
n2 = int(input('Ingrese el segundo número:\n'))

operacion = int(input('Ingrese el número de la operación que desea aplicar:\n1 Suma\n2 Resta\n3 Multiplicación\n'))

sum = n1 + n2
resta = n1 - n2
multi = n1 * n2

msj = 'El resultado de la operación seleccionada es: {}'

if operacion == 1:
    result = sum
    print(msj.format(result))
elif operacion == 2:
    result = resta
    print(msj.format(result))
elif operacion == 3:
    result = multi
    print(msj.format(result))
else: 
    print('Opción incorrecta, ingrese el número que aparece en el listado')