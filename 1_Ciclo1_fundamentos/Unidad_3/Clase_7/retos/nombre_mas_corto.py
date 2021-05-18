import diccionario as data

nombreCorto = ''
cantidad = len(data.devs[0])
for name in data.devs.values():
    if cantidad > len(name):
        cantidad = len(name)
        nombreCorto = name

print(nombreCorto)
