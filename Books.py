# Основной класс
class Library:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __add__(self):
        return {
            'name': self.name,
            'count': self.count
        }


class Psychology_books(Library):
    def __init__(self, name, count, author):
        super().__init__(name, count)
        self.author = author

    def __add__(self):
        psychology_books = super().__add__()
        psychology_books.update({
            'author': self.author
        })
        return psychology_books


class Math_books(Library):
    def __init__(self, name, count, author):
        super().__init__(name, count)
        self.author = author

    def __add__(self):
        math_books = super().__add__()
        math_books.update({
            'author': self.author
        })
        return math_books


class Literature_books(Library):
    def __init__(self, name, count, author):
        super().__init__(name, count)
        self.author = author

    def __add__(self):
        literature_books = super().__add__()
        literature_books.update({
            'author': self.author
        })
        return literature_books


class Science_books(Library):
    def __init__(self, name, count, author):
        super().__init__(name, count)
        self.author = author

    def __add__(self):
        science_books = super().__add__()
        science_books.update({
            'author': self.author
        })
        return science_books