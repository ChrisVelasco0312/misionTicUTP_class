# Los que ganan más de tres salarios minimos vigentes en colombia:
# Salario minimo legal : 908526

from developers import devs

salario_minimo = 908526

# for dev in devs:
#     print(dev['Salario'])

# print(salario_minimo * 3)

mas_de_tres_salarios = [
    dev for dev in devs if dev['Salario'] >= salario_minimo * 3
]
mas_bono_experiencia = [
    dev['Salario'] + 300000 for dev in devs if dev['Salario'] <= 2500000 and dev['years'] >= 3
]

# print(mas_de_tres_salarios)
print(mas_bono_experiencia)
