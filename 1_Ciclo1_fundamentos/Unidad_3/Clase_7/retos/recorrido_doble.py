import diccionario as data

# Ejemplo de recorrido doble en diccionarios
# Accediendo a cada valor y a cada caracter.

nombre = ""
count = 0
# devs.values() crea una lista con los valores.
for dev in data.devs.values():
    for letra in dev:
        # crea un string con todos los nombres
        nombre += letra
        # cuenta el total de caracteres de todos los nombres
        count += 1


print(nombre)
print(count)
