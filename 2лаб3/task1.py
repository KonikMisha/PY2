class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        journal().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Значение pages должно соответствовать типу int')
        if not pages > 0:
            raise ValueError('Значение pages должно быть положительным числом')
        self.pages = pages

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}. Количество страниц: {self.pages}"

    def __repr__(self):
        journal_repr = journal().__repr__()
        return f"{journal_repr}"


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        journal().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Значение duration должно соответствовать типу float')
        if not duration > 0:
            raise ValueError('duration должно быть положительным числом')
        self.duration = duration

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}. Продолжительность: {self.duration}"

    def __repr__(self):
        journal_repr = journal().__repr__()
        return f"{journal_repr}"
