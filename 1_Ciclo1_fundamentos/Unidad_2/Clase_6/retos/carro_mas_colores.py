import dict_carro as data
from funcion_mayor import mayor
"""
    Retornar carro con más colores disponibles, 
    usamos la función len()
"""

# Guardando colores en variables

sandero = len(data.carro['modelos'][1]['colores'])
kwid = len(data.carro['modelos'][2]['colores'])
duster = len(data.carro['modelos'][3]['colores'])
megan = len(data.carro['modelos'][4]['colores'])


def carro_mas_colores():
    return mayor(data, sandero, kwid, duster, megan)


print(carro_mas_colores())
