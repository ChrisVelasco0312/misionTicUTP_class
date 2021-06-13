import pandas as pd
from pandas.core.frame import DataFrame


def get_data_frame() -> DataFrame:
    return pd.read_csv('agenda.csv')


def read_agenda():
    print('-------------* Leer agenda *-------------\n')
    # leer agenda con pandas ||
    # lo organiza en un formato
    print(get_data_frame(), '\n \n')


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


# ----- Mi Solución ----
# def update_contact():
#     # Muestro los contactos registrados
#     print('Seleccione el contacto que desea actualizar: ')
#     print(get_data_frame()['name'])
#     print(len(get_data_frame()))
#     # Permito seleccionar uno de los contactos por su índice
#     selection = int(input('Selecciona el numero correspondiente: '))
#     new_df = get_data_frame()
#     # Creo una validación para que si se pasa de los contactos disponibles
#     # salga un error, igualmente con números negativos
#     if selection < len(new_df) and selection >= 0:
#         # Hago un try except para en caso de ingresar datos invalidos
#         # salga un error y vuelva a ejecutar la función
#         try:
#             # De esta forma se pide que cada dato sea actualizado
#             new_df.loc[selection, 'name'] = input('Nuevo nombre: ')
#             new_df.loc[selection, 'cel'] = int(input('Nuevo cel: '))
#             new_df.loc[selection, 'email'] = input('Nuevo email: ')
#             # se muestra un mensaje que despliega el contacto
#             # con los datos actualizados
#             print('\nContacto actualizado: ')
#             print(new_df.loc[selection, ['name', 'email', 'cel']])
#             new_df.to_csv('agenda.csv', index=False)
#         except:
#             print('Datos incorrectos, pruebe de nuevo: ')
#             update_contact()
#     else:
#         print('El numero excede las opciones disponibles, ' +
#               'trate nuevamente... ')
#         update_contact()


# ----- Solución de clase ----
def update_contact():
    read_agenda()
    # Se pide el id:
    id = int(input('Escribe el id: '))
    # Se crea un menú de opciones:
    option = input("""
            Qué deseas editar:
                1- Nombre
                2- Celular
                3- Email""" + '\n')
    if option == '1':
        data_F = get_data_frame()
        data_F.loc[id, 'name'] = input('Nombre: ')
        data_F.to_csv('agenda.csv', index=False)
    elif option == '2':
        data_F = get_data_frame()
        data_F.loc[id, 'cel'] = int(input('Celular: '))
        data_F.to_csv('agenda.csv', index=False)
    elif option == '3':
        data_F = get_data_frame()
        data_F.loc[id, 'email'] = input('Email: ')
        data_F.to_csv('agenda.csv', index=False)


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


# ----- Solución de clase ----- #
# def search_by_name():
#     name = input('Buscar: ')
#     new_df = get_data_frame().loc[lambda contact: contact['name'].
#                                   str.contains(name), :]
#     print(new_df)

# --- Mi Solución ----
def remove_contact():
    # Muestro los contactos disponibles
    read_agenda()
    # Pide el índice del contacto a eliminar
    try:
        selection = int(input('Seleccione el contacto que quiere eliminar: '))
    except:
        print('Selección invalida intente de nuevo...')
        remove_contact()

    # Creo un nuevo dataframe.
    new_df = get_data_frame()

    # Valido si está seguro de eliminar
    if selection > -1:
        ok = input('¿Está seguro de elminar este contacto? (S/N): ').lower()

        if ok == 's':
            # Elimino la fila con la función drop
            new_df = new_df.drop([selection])
            # Creo el nuevo csv con los cambios nuevos.
            new_df.to_csv('agenda.csv', index=False)
            read_agenda()
        elif ok == 'n':
            exit()
        else:
            print('Opción no valida...')
            remove_contact()


def show_menu():
    print(
        """
        -------* BIENVENIDO A SU AGENDA *-------
        ----------* elija su opción *-----------

            1- Crear Contacto
            2- Leer agenda
            3- Buscar por nombre
            4- Actualizar contacto
            5- Eliminar contacto
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
    elif option == '5':
        remove_contact()
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
