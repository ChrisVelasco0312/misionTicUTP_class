#mini_reto_2.py mi solución
"""
    Crear una función que reciba 4 parametros:
        edad, semanas_cotizadas, monto, hombre o mujer
        
        - Según la edad y semanas cotizadas evalue la pensión
        por el 90% del monto
        - Si es hombre la edad mínima es 63, si es mujer
        la edad mínima es 58
        - Las semanas cotizadas deberán ser mínimo 250
"""

def calcular_pension(edad, semanas_cotizadas, monto, sexo):
    sexo = sexo.lower() 

    if ((sexo == 'hombre' and edad >= 63) or (sexo=='mujer' and edad >= 58)) and (semanas_cotizadas >= 250):
        pension = monto * 0.90
        print(f"Tiene derecho a pensión por valor de: {pension}")
    else:
        print("No tiene derecho a pensión")

