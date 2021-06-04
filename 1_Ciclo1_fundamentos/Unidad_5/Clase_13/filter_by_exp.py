import pandas as pd

devs = [
    {'cc': 1540, 'nombre': 'Miguel', 'Salario': 2600000, 'years': 5,
     'lenguajes': {0: 'Python', 1: 'Java'}},
    {'cc': 1556, 'nombre': 'Cristian', 'Salario': 2500000, 'years': 2,
     'lenguajes': {0: 'Python', 1: 'Javascript', 2: 'Rust'}},
    {'cc': 2556, 'nombre': 'Juan Ignacio', 'Salario': 2400000, 'years': 3,
     'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
    {'cc': 1340, 'nombre': 'Nicolas', 'Salario': 2400000, 'years': 4,
     'lenguajes': {0: 'Python', 1: 'C++', 2: 'C#'}},
    {'cc': 1526, 'nombre': 'Sendy', 'Salario': 2400000, 'years': 5,
     'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
    {'cc': 2516, 'nombre': 'Santiago', 'Salario': 2600000, 'years': 5,
        'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
    {'cc': 1547, 'nombre': 'David', 'Salario': 2500000, 'years': 3,
     'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
    {'cc': 1556, 'nombre': 'Milton', 'Salario': 2800000, 'years': 6,
     'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
    {'cc': 5586, 'nombre': 'Jinneth', 'Salario': 2800000, 'years': 2,
     'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
    {'cc': 3556, 'nombre': 'Alejandro', 'Salario': 2700000, 'years': 1,
     'lenguajes': {0: 'Python', 1: 'Ruby', 2: 'Swift'}},
]

devs2 = pd.DataFrame(devs)

devs_read_csv = pd.read_csv('devs.csv')

# print(devs_read_csv.loc[lambda dev: dev['years'] >= 4, :])
# print(devs_read_csv.loc[lambda dev: (dev['years'] <
#                                      4 and dev['Salario'] >= 2400000), :])

devs3 = pd.concat([devs2, pd.DataFrame([lang for lang in devs2['lenguajes']])],
                  axis=1)

print(devs3)
