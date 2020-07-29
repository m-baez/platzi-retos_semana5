# Reto # 6 - Cuenta regresiva

"""Pide a tu usuario un número, después imprime una cuenta regresiva uno a uno, desde ese número hasta 0. Esto aplica también para números negativos."""

userNumber = int(input('Escribe un número y presiona ENTER: '))
if userNumber > 0:
    for i in range(userNumber):
        userNumber = userNumber - 1
        print(userNumber)
else:
    for i in range(userNumber, 0):
        userNumber = userNumber + 1
        print(userNumber)
