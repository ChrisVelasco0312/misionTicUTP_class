class Book:
    def __init__(self, title, author, price, room) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.room = room

    def show(self):
        return f'Título: {self.title}\nAutor: {self.author}' +\
                f'\nPrecio: {self.price}\n'

    def iva(self):
        return self.price * 0.19


class Room:
    def __init__(self, name, capacity, id) -> None:
        self.name = name
        self.capacity = capacity
        self.id = id
        self.books = []

    def add_book(self, title, author, price):
        if len(self.books) <= self.capacity:
            book = Book(title, author, price, self.id)
            self.books.append(book)
        else:
            print('!No se pueden agregar más libros!')


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


biblioteca = Library('Banco de la República')

sala_1 = Room('Novelas', 3, 1)

biblioteca.add_room(sala_1)

biblioteca.rooms[0].add_book('El señor de las moscas',
                             'William Golding', 70000)
biblioteca.rooms[0].add_book('Factatum', 'Charles Bukowski', 60000)
biblioteca.rooms[0].add_book('Pigmeo', 'Chuck Palahniuk', 85000)


for book in sala_1.books:
    print(book.show())


# libro_1 = Book('El señor de las moscas', 'William Golding', 70000)
# libro_2 = Book('Factatum', 'Charles Bukowski', 80000)

# # data = libro_1.show()
# # data2 = libro_2.show()
# data = libro_1.iva()
# data2 = libro_2.iva()


# print(data)
# print(data2)
