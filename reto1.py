# Reto #1 - Curso favorito

"""Pide a tu usuario que indique cual es su curso favorito de Platzi e imprímelo en pantalla 8 veces.
¿Por qué 8 veces? Porque este año Platzi cumplió 8 años 😉"""

curse = str(input('¿Cúal es tu curso favorito de Platzi? '))
for x in range(1, 9):
    print('#%d.- %s' % (x, curse.capitalize()))
