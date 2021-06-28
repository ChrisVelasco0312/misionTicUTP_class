import dict_carro as data

"""
    Retornar si existen carros con el mismo precio
"""

# Guardando precio en variables

sandero = data.carro['modelos'][1]['precio']
kwid = data.carro['modelos'][2]['precio']
duster = data.carro['modelos'][3]['precio']
megan = data.carro['modelos'][4]['precio']


def carro_mismo_precio():
    if sandero == kwid or sandero == duster or sandero == megan \
       or kwid == duster or kwid == megan or duster == megan:
        return True
    else:
        return False


print(carro_mismo_precio())
