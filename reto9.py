# Reto #9 - Recta numérica

"""Escribe un programa donde preguntes a tu usuario si desea una recta numérica positiva o negativa, después pide un número que servirá como límite e imprime todos los números de uno en uno partiendo desde el cero."""

user = str(input('¿Recta numérica positiva o negativa? (p/n) ').lower())
numb = int(input('Escribe un número que servirá como límite: '))
if user == 'p':
    for i in range(numb+1):
        print(i)
elif user == 'n':
    for i in range(numb+1):
        numb = numb - 1
        print(-1*i)
