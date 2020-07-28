# Reto #4 - Animal en columna ‘n’ veces

"""Toma como base el reto anterior, pide a tu usuario que indique su animal favorito y después muéstralo con un caracter por línea. Esto debe repetirse un número de veces que ya hayas preguntado a tu usuario."""

animal = str(input('¿Cúal es tu animal favorito? '))
times = int(input('¿Cúantas veces lo quieres repetir? '))
for x in range(times):
    for y in animal:
        print(y)
