import doctest
from datetime import datetime


class MoviesList:
    def __init__(self, author_name: str, movies=None):
        """
        Создание и подготовка к работе объекта "Список фильмов"

        :param author_name: Имя владельца списка
        :param movies: Список фильмов (по умолчанию None)

        Примеры:
        >>> movieslist1 = MoviesList('Neonila')  # инициализация экземпляра класса
        >>> movieslist2 = MoviesList('Neonila', ['Iron man', 'Lord of the rings 1'])  # инициализация экземпляра класса
        """
        if not isinstance(author_name, str):
            raise TypeError("Имя владельца списка должно быть типа str")
        self.author_name = author_name

        self.movies = movies if movies is not None else []

    def add_movie(self, new_movie: str) -> None:
        """
        Функция которая добавляет в список новый фильм

        :param new_movie: Добавляемый в список фильм
        :return: None
        :raise ValueError: Если данный фильм уже присутствует в списке, то вызываем ошибку

        Примеры:
        >>> movieslist2 = MoviesList('Neonila', ['Iron man', 'Lord of the rings 1'])
        >>> movieslist2.add_movie('Lord of the rings 2')
        """
        if not isinstance(new_movie, str):
            raise TypeError("Название фильма должно быть типа str")
        ...

    def delete_movie(self, movie_to_delete: str) -> None:
        """
        Функция которая удаляет из списка фильм

        :param movie_to_delete: Удаляемый из списка фильм
        :return: None
        :raise ValueError: Если данный фильм отсутствует в списке, то вызываем ошибку

        Примеры:
        >>> movieslist2 = MoviesList('Neonila', ['Iron man', 'Lord of the rings 1'])
        >>> movieslist2.delete_movie('Iron man')
        """
        if not isinstance(movie_to_delete, str):
            raise TypeError("Название фильма должно быть типа str")
        ...


class Flower:
    def __init__(self, name: str, color: str, last_watered_date: datetime):
        """
        Создание и подготовка к работе объекта "Цветок"

        :param name: Название цветка
        :param color: Цвет цветка
        :param last_watered_date: Дата последнего полива

        Примеры:
        >>> flower = Flower("Rose", "Pink", datetime(2023, 1, 23))  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название цветка должно быть типа str")
        self.name = name

        if not isinstance(color, str):
            raise TypeError("Цвет цветка должен быть типа str")
        self.color = color

        if not isinstance(last_watered_date, datetime):
            raise TypeError("Параметр last_watered_date должен быть типа datetime")
        self.last_watered_date = last_watered_date

    def is_watered(self) -> bool:
        """
        Функция которая проверяет полит ли цветок

        :return: Является ли цветок политым

        Примеры:
        >>> flower = Flower("Rose", "Pink", datetime(2023, 1, 23))
        >>> flower.is_watered()
        """
        ...

    def water_the_flower(self, water: float) -> None:
        """
        Метод для полива цветка
        :param water: Объем воды для полива

        :raise ValueError: Если объем воды превышает допустимую для данного цветка величину, то вызываем ошибку
        :return: None

        Примеры:
        >>> flower = Flower("Rose", "Pink", datetime(2023, 1, 23))
        >>> flower.water_the_flower(500)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Объем воды должен быть типа int или float")
        if water <= 0:
            raise ValueError("Объем воды для полива должен положительным числом")
        ...


class Coffee:
    def __init__(self, coffee: int, water: float):
        """
        Создание и подготовка к работе объекта "Кофе"

        :param coffee: Количество кофе
        :param water: Количество воды

        Примеры:
        >>> my_coffee = Coffee(2, 200)  # инициализация экземпляра класса
        """
        if not isinstance(coffee, int):
            raise TypeError("Количество столовых ложек кофе должно быть типа int")
        if coffee <= 0:
            raise ValueError("Количество столовых ложек кофе должно быть положительным числом")
        self.coffee = coffee

        if not isinstance(water, (int, float)):
            raise TypeError("Объем воды должен быть типа int или float")
        if water <= 0:
            raise ValueError("Объем воды должен быть положительным числом")
        self.water = water

    def brew_coffee(self) -> None:
        """
        Функция которая варит кофе
        :return: None

        Примеры:
        >>> my_coffee = Coffee(2, 200)
        >>> my_coffee.brew_coffee()
        """
        ...

    def pour_coffee(self, cup: float, is_milk: bool) -> None:
        """
        Функция которая наливает кофе в чашку
        :return: None

        Примеры:
        >>> my_coffee = Coffee(2, 200)
        >>> my_coffee.brew_coffee()
        >>> my_coffee.pour_coffee(250, True)
        """
        if not isinstance(cup, (int, float)):
            raise TypeError("Объем чашки должен быть типа int или float")
        if cup <= 0:
            raise ValueError("Объем чашки должен быть положительным числом")

        if not isinstance(is_milk, bool):
            raise TypeError("Наличие или отсутствие молока должно быть типа bool")
        ...

    def add_milk(self, milk: float) -> None:
        """
        Функция для добавления молока
        :param milk: Объем добавляемого молока

        :raise ValueError: Если объем воды и молока превышает объем чашки, то вызываем ошибку
        :return: None

        Примеры:
        >>> my_coffee = Coffee(2, 200)
        >>> my_coffee.brew_coffee()
        >>> my_coffee.pour_coffee(250, True)
        >>> my_coffee.add_milk(20)
        """
        if not isinstance(milk, (int, float)):
            raise TypeError("Объем молока должен быть типа int или float")
        if milk < 0:
            raise ValueError("Объем молока не должен быть отрицательным числом")
        ...



if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass