# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
# pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
# puede ser calculada de la siguiente forma

n = int(input('Ingrese un número entero: '))

f = int((n * (n + 1) ) / 2)

print(f'El resultado es: {f}')
