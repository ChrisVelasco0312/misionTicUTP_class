#mini_reto.py mi solución

"""
    Dada la edad, asignar categoría del jugador:
        -Entre 10 y 14, Infantil
        -Entre 15 y 17, Juvenil
        -Entre 18 y 32, Profesional
        -Mayor a 33, Veterano
"""

edad = int(input('Ingrese la edad del jugador: '))

if edad >= 10 and edad <= 14:
    print('El jugador es de la categoría: Infantil')
elif edad >= 15 and edad <= 17:
    print('El jugador es de la categoría: Juvenil')
elif edad >= 18 and edad <= 32:
    print('El jugador es de la categoría: Profesional')
elif edad >= 33:
    print('El jugador es de la categoría: Veterano')
else:
    print('Edad invalida')
