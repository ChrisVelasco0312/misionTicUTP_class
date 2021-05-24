'''
    - ¿Que desarrollador sabe más lenguajes?
    - ¿Cuantos lenguajes más sabe el desarrollador?
    - En caso de que maneje más, ¿que lenguajes sabe uno que no sepa el otro?
    en caso de empate envíe un mensaje que especifique este caso
'''


from dict_desarrolladores import desarrolladores

# print(desarrolladores.items())
# print(desarrolladores[2]['habilidades']['lenguajes'])
# print(desarrolladores[1]['habilidades']['lenguajes'])
# print(len(desarrolladores[1]['habilidades']['lenguajes']))

dev_one = len(desarrolladores[1]['habilidades']['lenguajes'])
dev_two = len(desarrolladores[2]['habilidades']['lenguajes'])


def dev_more_languages(devs, p1, p2):
    dev_one_name = devs[1]['nombre']
    dev_two_name = devs[2]['nombre']

    if p1 > p2:
        print(
            f"{dev_one_name} sabe {p1 - p2} lenguajes más que {dev_two_name}"
        )
    elif p1 == p2:
        print(f"{dev_one_name} y {dev_two_name} saben los mismos lenguajes")
    else:
        print(
            f"{dev_two_name} sabe {p2 - p1} lenguajes más que {dev_one_name}"
        )

dev_more_languages(desarrolladores, dev_one, dev_two)
