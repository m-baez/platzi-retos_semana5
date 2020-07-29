# Reto #8 - Suma autorizada

"""Crearás un programa que pedirá a tu usuario 4 números, uno por uno. Al indicarlo preguntarás al usuario si desea sumarlo al total, si la respuesta es afirmativa se sumará. Al final debes mostrar el valor de la suma de aquellos números que fueron aceptados para la suma."""

res = 0
for i in range(4):
    num = int(input('Escribe un número y presiona ENTER: '))
    suma = input('¿Sumarás el número? y/n: ').lower()
    if suma == 'y':
        res = res + num
    else:
        pass
print(res)
