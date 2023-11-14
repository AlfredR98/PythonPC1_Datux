# Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
# último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
# verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.
cant_show = int(input('¿Cuantos shows ha visto en el último año?\n'))

if cant_show > 3:
    print('El usuario ha visto más de 3 shows')
else: print('El usuario NO ha visto más de 3 shows')