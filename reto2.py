# Reto #2 - Curso favorito ‘n’ veces

"""Toma el reto anterior, pero ahora pregunta al usuario cuantas veces quiere mostrar el mensaje.
¿Qué pasa si coloca cero como respuesta? 🤔"""

curse = str(input('¿Cúal es tu curso favorito de Platzi? '))
times = int(input('¿Cúantas veces lo quieres repetir? '))
for x in range(1, times+1):
    print('#%d.- %s' % (x, curse.capitalize()))
