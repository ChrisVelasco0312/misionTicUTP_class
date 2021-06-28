class Author:
    def __init__(self, name, birth) -> None:
        self.name = name
        self.birth = birth
        self.books = []

    def add_book(self, title, author, price):
        if len(self.books) <= self.capacity:
            book = Book(title, author, price, self.id)
            self.books.append(book)


class Book:
    def __init__(self, title, author, price, room) -> None:
        self.title = title
        self.author = author
        self.price = float(price)
        self.room = room

    def show(self):
        return f'Título: {self.title}\nAutor: {self.author}' +\
            f'\nPrecio: {self.price}\n'

    def iva(self):
        return self.price * 0.19


class Room:
    def __init__(self, id, name, capacity) -> None:
        self.name = name
        self.capacity = int(capacity)
        self.id = id
        self.books = []

    def add_book(self, title, author, price):
        if len(self.books) <= self.capacity:
            book = Book(title, author, price, self.id)
            self.books.append(book)
        else:
            print('!No se pueden agregar más libros!')

    def show(self):
        return f'Nombre: {self.name}, \nCapacidad: {self.capacity}'

    # def get_books(self):
    #     result = [book.show() for book in self.books]
    #     return result


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.rooms = []

    # def add_room(self, room):
    #     self.rooms.append(room)

    def add_room(self, name, capacity, id):
        room = Room(name, capacity, id)
        self.rooms.append(room)

    def get_rooms(self):
        result = [room.show() for room in self.rooms]
        return result

    def add_book(self, id, title, author, price):
        self.rooms[id].add_book(title, author, price)


# biblioteca = Library('Banco de la República')

# sala_1 = Room('Novelas', 3, 1)

# biblioteca.add_room(sala_1)

# biblioteca.rooms[0].add_book('El señor de las moscas',
#                              'William Golding', 70000)
# biblioteca.rooms[0].add_book('Factatum', 'Charles Bukowski', 60000)
# biblioteca.rooms[0].add_book('Pigmeo', 'Chuck Palahniuk', 85000)


# for book in sala_1.books:
#     print(book.show())
