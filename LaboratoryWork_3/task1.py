class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property  # геттер для атрибута name
    def name(self) -> str:
        return self._name

    @property  # геттер для атрибута author
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """Дочерний класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # наследуем базовый конструктор
        if pages <= 0:
            raise ValueError("Кол-во страниц в книге должно быть положительным")
        self._pages = pages

    @property  # геттер для атрибута pages
    def pages(self) -> int:
        return self._pages

    @pages.setter  # сеттер для атрибута pages
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Кол-во страниц в книге должно быть целым числом")
        if new_pages <= 0:
            raise ValueError("Кол-во страниц в книге должно быть положительным")
        self._pages = new_pages

    def __str__(self):
        return super().__str__()  # наследуем метод __str__ из базового класса

    def __repr__(self):  # перегружаем метод __repr__ для класса PaperBook
        return f"{self.__class__.__name__}(name={self.name!r}, " \
                                         f"author={self.author!r}, " \
                                         f"pages={self.pages})"


class AudioBook(Book):
    """Дочерний класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # наследуем базовый конструктор
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительной")
        self._duration = duration

    @property  # геттер для атрибута duration
    def duration(self):
        return self._duration

    @duration.setter  # сеттер для атрибута duration
    def duration(self, new_duration: float):
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительной")
        self._duration = new_duration

    def __str__(self):
        return super().__str__()  # наследуем метод __str__ из базового класса

    def __repr__(self):  # перегружаем метод __repr__ для класса AudioBook
        return f"{self.__class__.__name__}(name={self.name!r}, " \
                                         f"author={self.author!r}, " \
                                         f"duration={self.duration})"

"""
Проверка работоспособности классов

if __name__ == "__main__":
    print("Базовый класс книги")

    book = Book("Метро 2033", "Д.Глуховский")
    print(book.__str__())
    print(book.__repr__())
    print(book.name)
    print(book.author)

    print("\nКласс бумажной книги")

    book_paper = PaperBook(book.name, book.author, 350)
    #book_paper = PaperBook(book.name, book.author, -350)  выдает ошибку
    print(book_paper.__str__())
    print(book_paper.__repr__())
    print(book_paper.pages)
    book_paper.pages = 400
    #book_paper.pages = -100  выдает ошибку
    print(book_paper.pages)

    print("\nКласс аудиокниги")

    book_audio = AudioBook(book.name, book.author, 13.5)
    print(book_audio.__str__())
    print(book_audio.__repr__())
    print(book_audio.duration)
    book_audio.duration = 24.7
    #book_audio.duration = -12.3  выдает ошибку
    print(book_audio.duration)
"""

