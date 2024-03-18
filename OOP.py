#ООП интернет магазин
class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author'):
            if type(value) is not str:
                raise TypeError("неверный тип присваиваемых данных")
        else:
            if type(value) is not int:
                raise TypeError("неверный тип присваиваемых данных")
        return object.__setattr__(self, key, value)


book = Book('Python OOП', 'Автор', 123, 2024)
print(book.title)