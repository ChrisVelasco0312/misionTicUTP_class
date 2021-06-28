from developers import devs

# Filtrar la lista con los desarrolladores cuyo nombre empiece por s o termine en o

filter_devs = list(filter(lambda devs: devs['nombre'][0].lower() == 's'
                          or devs['nombre'][-1].lower() == 'o', devs))

print(filter_devs)
