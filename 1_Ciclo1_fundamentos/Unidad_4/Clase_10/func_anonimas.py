def verificar_palindromo(palabra):
    palabra = palabra.lower().replace(' ', '')
    return palabra == palabra[::-1]

# es_palindromo = lambda palabra: palabra == palabra[::-1]


print(verificar_palindromo('oso'))  # usando funcion tradicional
print(verificar_palindromo('luz azul'))  # usando funcion tradicional
# print(es_palindromo('ANA'))  # usando funcion anonima


# cuadrado = lambda num1 : num1 ** 2
def cuadrado(num1): return num1 ** 2


print(cuadrado(2))


# es_mayor = lambda edad: 'es mayor' if edad >= 18 else 'no es mayor'
def es_mayor(edad): return 'es mayor' if edad >= 18 else 'no es mayor'


print(es_mayor(10))
