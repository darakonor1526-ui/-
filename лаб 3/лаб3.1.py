class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self):
        return self.name

    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def pages(self):
        return self.pages

    def pages(self, value):
        if value <=0:
            raise ValueError("Количество страниц должно быть больше нуля")
        if not isinstance(value, int):
            raise TypeError ("Количество страниц должно быть целым")
        self.pages=value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def duration(self):
        return self.duration

    def duration(self, value):
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть целым")
        self.duration = float(value)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
