"""
    Un bus viaja a 30km/h en promedio, 90km
    recoger pasajeros demora 2 minutos por pasajero
    bajar pasajero demora 1 minuto

    Cuantos minutos demora el bus, dada una cantidad de pasajeros que se subieron
    y otra cantidad de pasajeros que se bajaron
"""


def calc_minutes_bus(passengers_up, passengers_down):
    passengers_minutes = (passengers_up * 2) + passengers_down
    route_minutes = (90 / 30) * 60

    result = route_minutes + passengers_minutes
    message = f"The bus takes {result} minutes to arrive"
    print(message)


calc_minutes_bus(5, 2)
