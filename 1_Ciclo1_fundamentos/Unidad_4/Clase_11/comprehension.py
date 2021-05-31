# lista = []


# for i in range(1, 101):
#     lista.append(i)

lista = [i for i in range(1, 101)]

# print(lista)

nons = [number*number for number in range(1, 101) if number % 2 == 1]

print(nons)

# ----------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = [i for i in numbers if i % 2 == 0]

print(odds)

# ----------------------------------------------------------------

# sort function

notes = [3.2, 4.1, 2.9, 1, 5, 4.5, 3.3, 2.8, 1.5]
notes.sort(reverse=True)

print(notes)

notes.reverse()
print(notes)
