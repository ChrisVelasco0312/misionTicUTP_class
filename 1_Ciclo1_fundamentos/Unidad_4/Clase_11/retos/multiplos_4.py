multiples_four = [i for i in range(1, 501) if i % 4 == 0]
multiples_three = [i for i in range(1, 501) if i % 3 == 0]

print("Multiples of four: ", multiples_four)
print("Multiples of three: ", multiples_three)

notInList = [i for i in multiples_four if i not in multiples_three]

print("Not in multiples three", notInList)

# El cuadrado de los múltiplos de 3 que esté en los múltiplos de 4

square_three_in_four = [
    num**2 for num in multiples_three if num**2 in multiples_four]

print("solución: ", square_three_in_four)
