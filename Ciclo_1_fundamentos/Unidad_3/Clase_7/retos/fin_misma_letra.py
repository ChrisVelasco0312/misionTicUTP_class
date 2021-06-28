import diccionario as data

# nombres que terminen en la misma letra

for key, dev in data.devs.items():
    for key2, dev2 in data.devs.items():
        if dev[-1] == dev2[-1] and key != key2:
            print(dev2)
