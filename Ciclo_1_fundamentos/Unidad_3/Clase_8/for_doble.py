numeros = [11, 42, 63, 81, 21, 12, 5, 8, 9]

# for numero in numeros:
#     for numero2 in numeros:
#         print(numero, numero2)

for numero in numeros:
    for numero2 in numeros:
        if numero2 % numero == 0 and numeros.index(numero2) != numeros.index(numero):
            print(f"{numero2} es multiplo de {numero}")

# con ciclo while es:

i = 0
while i < len(numeros):
    j = 0
    while j < len(numeros):
        if numeros[i] % numeros[j] == 0 and numeros[i] != numeros[j]:
            print(f"{numeros[i]} es multiplo de {numeros[j]}")
        j += 1
    i += 1
