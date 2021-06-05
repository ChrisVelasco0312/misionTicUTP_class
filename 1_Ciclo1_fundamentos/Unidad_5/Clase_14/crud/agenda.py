import pandas as pd
from pandas.core.frame import DataFrame


def get_data_frame() -> DataFrame:
    return pd.read_csv('agenda.csv')


def read_agenda():
    print('-------------* Leer agenda *-------------\n')
    # leer agenda con pandas ||
    # lo organiza en un formato
    print(get_data_frame(), '\n \n')
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


def update_contact():
    print('Seleccione el contacto que desea actualizar: ')
    print(get_data_frame()['name'])
    selection = int(input('Selecciona el numero correspondiente: '))
    new_df = get_data_frame()
    new_df.loc[selection, 'cel'] = int(input('Nuevo número: '))
    print('Contacto actualizado: ')
    print(new_df.loc[selection, ['cel', 'name']])
    new_df.to_csv('agenda.csv', index=False)
    # print(get_data_frame().loc[selection, 'cel'])


# ---------- Mi solución-----------------
def search_by_name():
    # se pide el nombre y se convierte en minúsculas
    search = input('Digite el nombre: ').lower()

    # leemos los datos y pasamos la columna name a los índices
    agenda_data = get_data_frame()
    agenda_name_indexed = agenda_data.set_index('name')

    # con un map convertimos todos los nombres de la lista en minúsculas
    names = list(map(lambda name: name.lower(), list(agenda_data['name'])))

    # con el metodo find guardamos las ocurrencias en una variable
    ocurrences = list(filter(lambda name: name.find(
        search) >= 0, names))

    # imprimimos convirtiendo cada inicial de la lista
    # en una capital o mayuscula
    # para que pueda encontrarlo en el dataframe a través de loc
    if ocurrences != []:
        print(
            agenda_name_indexed.loc[
                list(map(lambda name: name.capitalize(), ocurrences))
            ]
        )
    else:
        print('Nombre no encontrado intente con otro: ')
        search_by_name()


def show_menu():
    print(
        """
        -------* BIENVENIDO A SU AGENDA *-------
        ----------* elija su opción *-----------

            1- Crear Contacto
            2- Leer agenda
            3- Buscar por nombre
            4- Actualizar número celular
            9- Salir

        """
    )
    option = input('Digite una opción: ')
    print('\n \n')
    if option == '1':
        create_contact()
    elif option == '2':
        read_agenda()
    elif option == '3':
        search_by_name()
    elif option == '4':
        update_contact()
    elif option == '9':
        exit()


# Crear el entry point
def run():
    show_menu()
    run()


if __name__ == '__main__':
    # crear un dataframe
    # df = pd.DataFrame(columns=['name', 'cel', 'email'])
    # crear un archivo .csv desde el dataframe
    # df.to_csv('agenda.csv', index=False)
    run()
