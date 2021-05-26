numeros = [11, 42, 63, 81, 21, 12, 5, 8, 9]


def traer_primer_multiplo(parametro):
    resultado = 0
    for numero in numeros:
        if numero % parametro == 0:
            resultado = numero
            break
    return resultado


print(traer_primer_multiplo(5))
