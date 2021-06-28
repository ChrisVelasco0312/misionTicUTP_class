import numpy as np

a = np.array([5, 7, 11])
b = np.array([[5, 7, 11],
              [10, 25, 67]])

# print(a)
# print(b)


myArray = np.array([[num for num in range(10, 501)],
                    [num for num in range(10, 501)]])

# print(myArray)

c = np.arange(14).reshape(2, 7)

# for list_num in c:
#     for num in list_num:
#         print(num)

# for num in c.flat:
#     print(num)

# print(c.size)


def llenar(num1, num2):
    return 2*num1+num2


myArray2 = np.fromfunction(llenar, (4, 4), dtype=int)

print(myArray2)
