# agregar un año de experiencia a todos los desarrolladores con map
from developers import devs


def plus_one_year(dev):
    dev['years'] += 1
    return dev


devs_update = list(map(plus_one_year, devs))
print(devs_update)
