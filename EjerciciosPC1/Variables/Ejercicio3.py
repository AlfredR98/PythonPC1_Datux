# la empresa de logística les cobra por peso de cada paquete así que deben 
# calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
# último pedido y calcule el peso total del paquete que será enviado.

muñeco = int(input('¿Cuantos muñecos se vendieron?\n'))
payaso = int(input('¿Cuantos payasos se vendieron?\n'))

peso_muñeco = muñeco * 75
peso_payaso = payaso * 112

print(f'El peso del paquete de los muñecos es {peso_muñeco}g y el paquete de los payasos es {peso_payaso}g')

