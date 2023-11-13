#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

consumo = float(input('¿Cuanto fue su consumo?\n'))
propina = float(input('¿Cuanto de propina en porcentaje(%) desea dejar al mesero?\n'))

dinero = consumo * (propina/100)

print(f'Debe dejar una propina de: S/.{dinero:.2f}')
