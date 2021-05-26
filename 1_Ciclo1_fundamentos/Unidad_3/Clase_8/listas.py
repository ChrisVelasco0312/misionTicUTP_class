list = []
# Siempre nombrar en plural
# el nombre tiene que decir que guarda.
numbers = [11, 25, 50, 11]
letras = ['c', 'r', 'i', 's']
# Las listas guardan datos
# Pueden guardar diferentes tipos de datos
mixed = ['Sapo', 7, 8.5, True]

# Indices en las listas,
# nos permiten acceder a los elementos

print(numbers[0])
print(mixed[3])

# METODOS

numbers.append(43)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.count(11))

numbers.remove(11)
print(numbers)

numbers.insert(2, 67)
print(numbers)

print(numbers.index(67))
