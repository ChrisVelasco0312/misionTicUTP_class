"""
    Una caja de aguacates Hass debe pesar en promedio 10kg.
    Cada aguacate pesa en promedio 0.25kg.
    Un arbol de aguacate da en promedio 40 aguacates por cocecha.


    Dado el peso en toneladas de un cargamento, crear un algoritmo 
    capaz de calcular el numero de arboles de aguacate Hass de donde 
    se recogieron los aguacates para este cargamento.

    notas: 
        1 tonelada = 1000 kg
        1 caja de aguacates hass = 10kg
        1000kg/10kg = 100 cajas son 1 tonelada
        10 / 0.25 = 40 aguacates en un arbol caben en una caja
        100 arboles son 1 tonelada de aguacates.

    parametros:
    ----------
    toneladas (int): número de toneladas del cargamento
    
    retorna:
    str: cadena de caracteres de la forma 
    'Para completar {toneladas} toneladas del cargamento se recogieron {aguacates} 
    aguacates de {arboles} arboles'
"""

from operaciones import calcular_aguacates, calcular_arboles


def resultado(toneladas):
    arboles = calcular_arboles(toneladas)
    aguacates = calcular_aguacates(arboles)
    return f"""
    Para completar {toneladas} toneladas del cargamento
    se recogieron {aguacates} aguacates de {arboles} arboles
    """


print(resultado(4))
