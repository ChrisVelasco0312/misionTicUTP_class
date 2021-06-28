import easygui as eg
import classes as cl


biblioteca = cl.Library('BiblioTK')


def menu():
    msg = "Menu de opciones"
    title = f"{biblioteca.name}"
    choices = ['Agregar', 'Listar']
    window = eg.buttonbox(msg=msg, title=title, choices=choices)

    if window == choices[0]:
        add_room()
    elif window == choices[1]:
        list_rooms()


def view_room(id):
    msg = 'Menú de opciones: '
    title = f'{biblioteca.name}: sala {biblioteca.rooms[id].name}'
    choices = ['Agregar Libro', 'Listar Libros', 'Menú Principal']
    window = eg.buttonbox(msg, title, choices)

    if window == choices[0]:
        add_book(id)
    elif window == choices[1]:
        pass
    elif window == choices[2]:
        menu()


def add_book(id):
    msg = 'Crea un libro \n Ingresando los valores: '
    title = f'{biblioteca.rooms[id].name}: Agregar libro'
    field_names = ['Título', 'Autor', 'Precio']
    field_values = []
    field_values = eg.multenterbox(msg, title, field_names)

    if field_values is None:
        menu()
    elif field_values[0] == '' or field_values[1] == '' or field_values[2] == '':
        eg.msgbox('Debe llenar todos los campos! ')
        add_book(id)
    else:
        # field_values.append(id)
        biblioteca.add_book(
            id, field_values[0], field_values[1], field_values[2])
        view_room(id)


# def room_menu(index):
#     room_name = biblioteca.rooms[index].name
#     msg = f'Sala: {room_name}'
#     title = f'{biblioteca.name}: Sala -> {room_name}'
#     choices = ['Agregar libro', 'Listar libros', 'Menú Principal']
#     window = eg.buttonbox(msg, title, choices)

#     if window == choices[0]:
#         add_book(index)
#     elif window == choices[1]:
#         list_books(index, room_name)
#     elif window == choices[2]:
#         menu()


# def list_books(index, room_name):
#     msg = f'Listado de libros en sala {room_name}'
#     title = f'{biblioteca.name}: Libros sala -> {room_name}'
#     choices = biblioteca.rooms[index].get_books()
#     index = eg.indexbox(msg, title, choices)

#     if index is None:
#         menu()
#     elif index >= 0:
#         menu()


def list_rooms():
    msg = 'Listado de salas'
    title = f'{biblioteca.name}: Salas'
    choices = biblioteca.get_rooms()
    index = eg.indexbox(msg, title, choices)
    # room_menu(index)
    if index is None:
        menu()
    else:
        view_room(index)


# def add_book(index):
#     msg = f'Agregar libro: '
#     title = f' sala: {biblioteca.rooms[index].name}'
#     field_names = ['Title', 'Author', 'Price']
#     field_values = eg.multenterbox(msg, title, field_names)

#     biblioteca.rooms[index].add_book(
#         field_values[0], field_values[1], field_values[2])

#     room_menu(index)


def add_room():
    msg = 'Crea una sala \n ingresando los valors de la sala'
    title = f'{biblioteca.name}: Agregar sala'
    field_names = ['Id', 'Nombre', 'Capacidad']
    field_values = []
    field_values = eg.multenterbox(msg, title, field_names)

    if field_values is None:
        menu()
    elif field_values[0] == '' or field_names[1] == '' or field_values[2] == '':
        menu()
    else:
        biblioteca.add_room(field_values[0], field_values[1], field_values[2])
        menu()


def run():
    menu()


if __name__ == '__main__':
    run()
