import diccionario as data

# Ver cual nombre se repite
for key, dev in data.devs.items():
    for key2, dev2 in data.devs.items():
        if dev == dev2 and key != key2:
            print(dev2)
