import pandas as pd


def read_agenda():
    print('-------------* Leer agenda *-------------\n')
    # leer agenda con pandas ||
    # lo organiza en un formato
    rd = pd.read_csv('agenda.csv')
    print(rd, '\n \n')
    # Sale de la agenda
    exit()


def create_contact():
    """
        Requiere, nombre, 
        numero de teléfono
        y un correo
    """
    # Se piden los datos
    name = input('Nombre: ')
    cel = input('Celular: ')
    email = input('E-Mail: ')

    # Se abre el archivo .csv
    # creado en ejecución
    fr = open('agenda.csv', 'a')
    # Crea una linea nueva con los datos
    fr.write(f'\n{name},{cel},{email}')
    # Cierra el archivo -- importante hacerlo siempre
    fr.close()


def show_menu():
    print(
        """
        -------* BIENVENIDO A SU AGENDA *-------
        ----------* elija su opción *-----------

            1- Crear Contacto
            2- Leer agenda
            9- Salir

        """
    )
    option = input('Digite una opción: ')
    print('\n \n')
    if option == '1':
        create_contact()
    elif option == '2':
        read_agenda()
    elif option == '9':
        exit()


# Crear el entry point
def run():
    show_menu()
    run()


if __name__ == '__main__':
    # # crear un dataframe
    # df = pd.DataFrame(columns=['name', 'cel', 'email'])
    # # crear un archivo .csv desde el dataframe
    # df.to_csv('agenda.csv', index=False)
    run()
