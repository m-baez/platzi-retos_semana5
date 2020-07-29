# Reto #5 - Tabla de multiplicar

"""Pide a tu usuario un número, luego de ello muestra la tabla de multiplicar de ese número del 1 al 10."""

print('tablas de multiplicar\n'.upper().center(41))
number = int(input('¿Qúe tabla de multiplicar quieres ver? '))
print('')
for x in range(1, 11):
    print('%d x %d = %d'.center(41) % (number, x, (number*x)))
print('')
