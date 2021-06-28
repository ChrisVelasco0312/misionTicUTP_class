devs = [{'cc': 1540, 'nombre': 'Mario', 'salario': 2500000},
        {'cc': 1556, 'nombre': 'Marco', 'salario': 2500000},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000}]


def create_dev():
    dev = {'cc': 0, 'nombre': '', 'salario': 0}
    try:
        dev['cc'] = int(input('Escriba la cedula del dev: '))
        dev['nombre'] = input('Escriba el nombre del dev: ')
        dev['salario'] = int(input('Escriba el salario del dev: '))
    except:
        print("Datos incorrectos vuelva a agregar el dev: ")
        create_dev()
    devs.append(dev)
    print(devs)


def list_devs():
    print('----------------------------------------------')
    print('--------------Listado de Devs-----------------')
    print('----------------------------------------------')
    for dev in devs:
        print(
            f'Cedula: {dev["cc"]}, Nombre: {dev["nombre"]}, Salario: {dev["salario"]}')


def search_by_name():
    name = input('Digite el nombre del desarrollador: ').lower()
    exist = False
    for dev in devs:
        if name in dev["nombre"].lower():
            print("Desarrollador encontrado: " +
                  f'Cedula: {dev["cc"]}, Nombre: {dev["nombre"]}, Salario: {dev["salario"]}')
            exist = True
    if not exist:
        print("No se encontraron desarrolladores")


def search_by_id():
    id = int(input('Digite la cédula del desarrollador: '))
    exist = False
    for dev in devs:
        if dev['cc'] == id:
            print("El dev que busca es:" +
                  f'Cedula: {dev["cc"]}, Nombre: {dev["nombre"]}, Salario: {dev["salario"]}')
            exist = True
    if not exist:
        print("El dev no se encuentra registrado")


def list_by_salary():
    salary = int(input('Escriba el salario: '))
    exist = True
    for dev in devs:
        if dev['salario'] >= salary:
            print(f"Desarrollador con salario mayor o igual a: {salary} : \n " +
                  f'Cedula: {dev["cc"]}, Nombre: {dev["nombre"]}, Salario: {dev["salario"]}')
            exist = True
    if not exist:
        print("No se encuentran desarrolladores con salarios mayores o iguales a:" + salary)


def set_options(option):
    if option == '1':
        create_dev()
    elif option == '2':
        list_devs()
    elif option == '3':
        search_by_id()
    elif option == '4':
        list_by_salary()
    elif option == '5':
        search_by_name()
    else:
        exit()


def run():
    print("""
    Escoge la acción que deseas realizar:
        1- Agregar un dev
        2- Listar devs
        3- Buscar desarrollador por cedula
        4- Listar desarrolladores por salario
        5- Buscar desarrollador por nombre
        9- Salir
    """)
    option = input("Digita el numero de la opcion: ")
    set_options(option)
    run()


if __name__ == "__main__":
    run()
    print(__name__)
