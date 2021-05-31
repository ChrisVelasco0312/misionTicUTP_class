numeros = [num for num in range(1, 101)]

par_impar = list(
    map(lambda numero: 'par' if numero % 2 == 0 else 'impar', numeros)
)

print(par_impar)
