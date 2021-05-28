def sum(num1=0, num2=0):
    return num1 + num2


def mult(num1=0, num2=0):
    return num1 * num2


def operate(function, num1, num2):
    return function(num1, num2)


print(operate(sum, 5, 9))
print(operate(mult, 5, 9))


# def h_order_function(function):
#     print(function())


# def decir_hola():
#     return 'Hola '


# def decir_mundo():
#     return 'mundo'


# h_order_function(decir_hola)
# h_order_function(decir_mundo)
