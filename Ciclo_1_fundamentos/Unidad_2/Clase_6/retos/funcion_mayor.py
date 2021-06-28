# Se crea una función que devuelva cual es el mayor valor de 4 valores.
def mayor(data, p1, p2, p3, p4):
    if(p1 >= p2 >= p3 >= p4):
        return data.carro['modelos'][1]['marca']
    elif(p2 >= p3 >= p4):
        return data.carro['modelos'][2]['marca']
    elif(p3 >= p4):
        return data.carro['modelos'][3]['marca']
    else:
        return data.carro['modelos'][4]['marca']
