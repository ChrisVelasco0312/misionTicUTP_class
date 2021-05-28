# Convertir una cadena de caracteres a una lista
cadena = 'Una cadena de texto'
lista = list(cadena)

print(lista)

# Convertir una cadena a una listas
print(''.join(lista))

# Convertir lista en tupla
tupla = tuple(lista)
print(tupla)

# Diccionarios

dict = {1: 'hi', 'a': 'world'}

print(list(dict))  # solo hace una lista con las llaves
print(list(dict.keys()))  # lo mismo que arriba
print(list(dict.values()))  # crea una lista con los values
print(list(dict.items()))  # crea una lista de tuplas con clave valores

tuple_items = list(dict.items())
tuple_1 = tuple_items[0]
print(list(tuple_1))
