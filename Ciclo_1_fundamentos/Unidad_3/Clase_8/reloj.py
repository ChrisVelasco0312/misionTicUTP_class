# Se inician la variables en 0
segundos = 0
minutos = 0

# Dada la condicion minutos < 60
# se anida otro ciclo donde se da la condición segundos < 60

while minutos < 60:
    while segundos < 60:
        segundos += 1  # Cada ciclo aumenta un segundo
    minutos += 1  # cuando sale del ciclo se aumenta un minuto
    segundos = 0  # cuando aumenta un minuto los segundos vuelven a 0
# el ciclo completaría una hora

# Este algoritmo solo se ejemplifica bajo el modo debug
