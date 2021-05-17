""" 
    Menu de programación de TV:
        1- Noticias
        2- Deportes
        3- Novelas
        4- Peliculas
"""

canal = int(input('Oprima el botón del canal: '))    

if canal == 1:
    print("Escogió el canal de noticias")
elif canal == 2:
    print('Escogió el canal de deportes')
elif canal == 3:
    print('Escogió el canal de novelas')
elif canal == 4:
    print('Escogió el canal de peliculas')
else:
    print('Canal no valido')


