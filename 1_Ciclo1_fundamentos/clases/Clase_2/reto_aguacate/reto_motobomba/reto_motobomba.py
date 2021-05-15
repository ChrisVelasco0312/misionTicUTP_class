"""
    Una motobomba llena 0.5m^3 en 3 minutos.
    dado el alto, el ancho y el largo de un tanque.
    determine cuanto tiempo en horas y en minutos 
    tarda en ser llenado el tanque

    parametros:
    ----------
    alto (int): alto del tanque
    ancho (int): ancho del tanque
    largo (int): largo del tanque

    El tanque es un prisma cúbico, el volumen se calcula así

    vol = Bh || area de la BASE por la altura

    el area de la BASE o B en este caso es = length * depth 

    entonces 

    volumen = (length * depth) * height
    
    en 3 minutos llena 0.5m

    donde

    volumen = (9 * 7) * 13
    819m3
    retorna:
    str: cadena de caracteres de la forma 
    'La motobomba llenará el tanque en {minutos} minutos, equivalente a {horas} horas'
"""


def calc_motor_pump_time(height, length, depth):
    volume = (length * depth) * height
    minutes = (volume/0.5) * 3
    hours = minutes / 60
    result = f"The motor pump fill the tank in {minutes} minutes, equal to {hours} hours "
    return result


print(calc_motor_pump_time(5, 2, 3))
print(calc_motor_pump_time(13, 9, 7))
