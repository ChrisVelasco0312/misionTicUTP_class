numeros = [11, 42, 63, 81, 21, 12, 5, 8, 9]

# for numero in numeros:
#     print(numero)

for numero in numeros:
    if numero % 9 == 0:
        print(numero)

# Saltar los múltiplos de 9 con continue, es decir
# devolver los que no son múltiplos de 9

for numero in numeros:
    if numero % 9 == 0:
        continue
    print(numero)
