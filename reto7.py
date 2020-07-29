# Reto #7 - Curso favorito, sin exagerar

"""Toma como base el Reto #2, pero agrega como condiciones las siguientes:

Si el número ‘n’ es mayor a 15, solo imprimirás el nombre del curso 3 veces e indicarás que ‘n’ es un número muy grande."""

curse = str(input('¿Cúal es tu curso favorito de Platzi? '))
times = int(input('¿Cúantas veces lo quieres repetir? '))
if times <= 15:
    for i in range(1, times+1):
        print('#%d.- %s' % (i, curse.capitalize()))
else:
    for i in range(1, 4):
        print('#%d.- %s' % (i, curse.capitalize()))
