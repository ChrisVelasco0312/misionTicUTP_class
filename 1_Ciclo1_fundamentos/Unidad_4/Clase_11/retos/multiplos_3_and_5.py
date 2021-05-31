# Lista con multiplos de tres que también son múltiplos de cinco

multiplos_tres = [num for num in range(
    1, 101) if num % 3 == 0 and num % 5 == 0]
print(multiplos_tres)
