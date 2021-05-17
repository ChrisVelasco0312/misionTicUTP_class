import dict_carro as data
from funcion_mayor import mayor

"""
    Cual es el carro más caro
"""

# Guardando precio en variables

sandero = data.carro['modelos'][1]['precio']
kwid = data.carro['modelos'][2]['precio']
duster = data.carro['modelos'][3]['precio']
megan = data.carro['modelos'][4]['precio']


# def carro_mas_caro():
#     if(sandero >= kwid >= duster >= megan):
#         return f"El carro más caro es: {data.carro['modelos'][1]['marca']}"
#     elif(kwid >= duster >= megan):
#         return f"El carro más caro es: {data.carro['modelos'][2]['marca']}"
#     elif(duster >= megan):
#         return f"El carro más caro es: {data.carro['modelos'][3]['marca']}"
#     else:
#         return f"El carro más caro es: {data.carro['modelos'][4]['marca']}"

# Funcion refactorizada con modulo funcion_mayor

def carro_mas_caro():
    return mayor(data, sandero, kwid, duster, megan)


print(carro_mas_caro())
