# TODO Написать 3 класса с документацией и аннотацией типов

class Shape:
    """
    Абстрактный класс для фигуры
    >>> class Circle(Shape):
    ...    def __init__(self, radius):
    ...        self.radius = radius
    ...
    ...    def area(self):
    ...        return 3.14 * self.radius ** 2
    ...    def slide_length(self):
    ...        return 3.14 * self.radius * 2
    ...
    >>> c = Circle(5)
    >>> c.area()
    78.5
    """

    def area(self):
        ...

    def side_length(self):
        ...

class Tree:
    """
    Дерево
    """

    def cut_down(self) -> None:
        """
        Симулирует срубание дерева
        :return: None
        """
        ...

    def water(self, volume: float) -> None:
        """
        Симулирует полив

        :param volume: Объем воды для полива в литрах
        :return: None

        >>> t = Tree()
        >>> t.water(15)
        """
        ...

class Computer:
    """
    Компьютер
    """

    def turn_on(self) -> None:
        """
        Включение компьютера

        :return: None

        >>> r = Computer()
        >>> r.turn_on()
        """
        ...

    def open_site(self, url: str) -> None:
        """
        Открыть сайт

        :param url: Адрес сайта
        :return: None

        >>> r = Computer()
        >>> r.open_site("https://dl-ido.spbstu.ru")
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
