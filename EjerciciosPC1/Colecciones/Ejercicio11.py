'''
Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,, 5]
'''

lista = [1, 1, 2, 3, 4, 4, 5, 1]
nueva_lista = list(set(lista))
print(nueva_lista)