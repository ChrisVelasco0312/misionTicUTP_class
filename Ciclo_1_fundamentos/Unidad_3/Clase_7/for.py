palabra = 'una palabra'

# Imprimir cada caracter de la cadena
for letra in palabra:
    print(letra)
# Con la funcion enumerate podemos acceder al indice de
# cada caracter e imprimirlo
for index, letra in enumerate(palabra):
    print(index, letra)
