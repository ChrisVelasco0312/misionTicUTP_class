import pandas as pd

devs = [
    {'cc': 1540, 'nombre': 'Miguel', 'Salario': 2600000, 'years': 5},
    {'cc': 1556, 'nombre': 'Cristian', 'Salario': 2500000, 'years': 2},
    {'cc': 2556, 'nombre': 'Juan Ignacio', 'Salario': 2400000, 'years': 3},
    {'cc': 1340, 'nombre': 'Nicolas', 'Salario': 2400000, 'years': 4},
    {'cc': 1526, 'nombre': 'Sendy', 'Salario': 2400000, 'years': 5},
    {'cc': 2516, 'nombre': 'Santiago', 'Salario': 2600000, 'years': 5},
    {'cc': 1547, 'nombre': 'David', 'Salario': 2500000, 'years': 3},
    {'cc': 1556, 'nombre': 'Milton', 'Salario': 2800000, 'years': 6},
    {'cc': 5586, 'nombre': 'Jinneth', 'Salario': 2800000, 'years': 2},
    {'cc': 3556, 'nombre': 'Alejandro', 'Salario': 2700000, 'years': 1},
]

devs2 = pd.DataFrame(devs, index=[dev['nombre'] for dev in devs])

# Buscar 2 elementos
print(devs2.loc[['Milton', 'Sendy']])

# Buscar por rango
print(devs2.loc['Sendy': 'Milton'])

# Buscar por rango mostrando elementos específicos
print(devs2.loc['Sendy': 'Milton', ['cc']])
