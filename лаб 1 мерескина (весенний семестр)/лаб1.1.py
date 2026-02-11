import doctest


class Notebook:
    def __init__(self, all_pages: float, scribbled_pages: float):
        """
        Создание и подготовка к работе объекта "Блокнот"

        :param  all_pages: Количество страниц
        :param scribbled_pages: Количество исписанных страниц

        Примеры:
        >>> notebook = Notebook(200, 0)  # инициализация экземпляра класса
        """
        if not isinstance(all_pages, (int)):
            raise TypeError("Количество страниц должно быть типа int")
        if all_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.all_pages = all_pages

        if not isinstance(scribbled_pages, (int, float)):
            raise TypeError("Количество исписанных страниц должно быть int или float")
        if scribbled_pages < 0:
            raise ValueError("Количество исписанных страниц не может быть отрицательным числом")
        self.scribbled_pages = scribbled_pages

    def is_empty_notebook(self) -> bool:
        """
        Функция которая проверяет является ли блокнот пустым

        :return: Является ли блокнот пустым

        Примеры:
        >>> notebook = Notebook(200, 0)
        >>> notebook.is_empty_notebook()
        """
        ...

    def write_in_notebook(self, pages: float) -> None:
        """
        Добавление воды в стакан.
        :param pages: Количество страниц, на которых будет написан текст

        :raise ValueError: Если количество будущих исписанных страниц превышает свободное место в блокноте, то вызываем ошибку

        Примеры:
        >>> notebook = Notebook(200, 85)
        >>> notebook.write_in_notebook(36,5)
        """
        if not isinstance(pages, (int, float)):
            raise TypeError("Количество будущих исписанных страниц должно быть типа int или float")
        if pages < 0:
            raise ValueError("Количество будущих исписанных страниц должно быть положительным числом")
        ...

    def tear_out_pages_from_notebook(self, torn_pages: float) -> None:
        """
        Вырывание страниц из блокнота.

        :param torn_pages: Количество вырванных страниц
        :raise ValueError: Если количество вырываемых страниц превышает количество страниц,
        то возвращается ошибка.

        :return: Объем реально вырванных страниц

        Примеры:
        >>> notebook = Notebook(200, 0)
        >>> notebook.tear_out_pages_from_notebook(23)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()