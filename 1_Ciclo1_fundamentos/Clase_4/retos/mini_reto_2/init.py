from pension import calcular_pension

def run():
    try:
        edad = int(input('Digite la edad: '))
        semanas_cotizadas = int(input('Digite las semanas cotizadas: '))
        monto = int(input('Digite el monto: '))
        sexo = str(input('Digite el sexo: '))

        calcular_pension(edad, semanas_cotizadas, monto, sexo)
    except:
        print("Hay un error en los datos, ingrese de nuevo")
        run()

    
if __name__ == '__main__':
    run()
