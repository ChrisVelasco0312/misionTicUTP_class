# función map

numeros = [num for num in range(1, 101)]

doble = list(
    map(lambda numero: numero * 2, numeros)
)

# print(numeros)
# print(doble)

# función filter

filtrada = list(filter(lambda numero: numero > 20 and numero < 55, numeros))

print(filtrada)
